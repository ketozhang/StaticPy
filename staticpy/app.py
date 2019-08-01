from pathlib import Path
from flask import (Flask, abort, redirect, render_template,
                   send_file, send_from_directory, url_for)
from shutil import rmtree, copyfile
from .config_handler import get_config
from .doc_builder import build_all
from .source_handler import get_frontmatter, get_subpages, get_fpath
from .log import log
from .globals import *


app = Flask(__name__, template_folder=TEMPLATE_PATH, static_folder=STATIC_PATH)


def run(*args, **kwargs):
    local = kwargs.pop('local', False)
    print(local)
    global SITE_URL
    if local:
        SITE_URL = ''

    app._run(*args, **kwargs)

app._run = app.run
app.run = run


########################
# META
########################
@app.context_processor
def global_var():
    # TODO SITE_URL best handled by a base config parser
    site_url = SITE_URL if SITE_URL else '/'
    if site_url[-1] != '/':
        site_url += '/'

    def parse_url(url):
        if url[0] == '/':
            url = SITE_URL + url
        return url

    def exists(file_or_path):
        """Check if the path exists in templates path."""
        fpath = TEMPLATE_PATH / get_fpath(file_or_path, resolve=False)
        return fpath.exists()

    var = dict(
        author=BASE_CONFIG['author'],
        debug=app.debug,
        navbar=BASE_CONFIG['navbar'],
        parse_url=parse_url,
        site_url=site_url,
        exists=exists,
        get_subpages=get_subpages,
        site_brand=BASE_CONFIG['site_brand'],
        site_title=BASE_CONFIG['site_title'],
        social_links=BASE_CONFIG['social_links'],
    )
    return var


@app.route('/favicon.ico')
def favicon():
    """Renders the favicon in /static/favicon.ico ."""
    return send_from_directory(STATIC_PATH, 'favicon.ico')


########################
# MAIN
########################

@app.route('/')
def home():
    """Renders the home page."""
    config = get_config('home')
    pages = {}  # TODO: Deprecate sitemap

    posts = config['posts']
    posts_dict = {}
    for post in posts:
        fm = get_frontmatter(post)
        posts_dict[post] = fm

    projects = config['projects']

    context = dict(
        pages=pages,
        posts=posts_dict,
        projects=projects
    )

    return render_template(config['template'], **context)


@app.route('/<file>')
def get_root_page(file):
    """Renders root level pages located in `TEMPLATE_PATH`/<file>.html .

    This is often useful for the pages "about" and "contacts".
    """
    fpath = get_fpath(TEMPLATE_PATH / file).relative_to(TEMPLATE_PATH)
    fpath = fpath.with_suffix(".html")
    return render_template(str(fpath))

@app.route(f'/<context>/<path:page>')
def get_page(context, page):
    """Routes all other page URLs. This supports both file and directory URL.

    For files (e.g., /notes/file.html), the content of the markdown file
    (e.g., /notes/file.md) is imported by the template.

    For directories (e.g., /notes/dir/), if there exists a index file, the
    directory is treated equivalent to the URL of the index file; otherwise,
    the template is used with no content. Note tha all directory URL have
    trailing slashes; its left to the server to always redirect directory URL
    witout trailing slashes.

    Context home pages (e.g., /note/index.html) are redirected to
    `url_for(<context>_home_page)`
    """
    log.info(f"Getting context: {context}, page: {page}")
    path = TEMPLATE_PATH / context / page

    # Redirect context home pages
    if path.name == 'index.html':
        return redirect(url_for(f'{context}_home_page'))

    # Attempt find the correct context
    try:
        _context = BASE_CONFIG['contexts'][context]
        source_path = PROJECT_PATH / _context['source_path']
    except KeyError as e:
        log.error(str(e) +
                  f', when attempting with args get_page({context}, {page}).')

    if (source_path / page).is_file() and path.suffix != '.html':   
        log.info(f"Fetching the file {str(source_path / page)}")
        return send_file(str(source_path / page))

    if page[-1] == '/':  # Handle directories
        if not path.is_dir():
            abort(404)
        _page = get_frontmatter(source_path / page / 'index.md')
        _page['url'] = f'/{context}/{page}'
        _page['parent'] = str(Path(_page['url']).parent) + '/'
        _page['subpages'] = get_subpages(_page['url'])
        _page['has_content'] = (path / 'index.html').exists()
        _page['content_path'] = str(
            (path / 'index.html').relative_to(TEMPLATE_PATH))
    elif path.with_suffix('.html').exists():  # Handle files
        path = path.with_suffix('.html')
        _page = get_frontmatter((source_path / page).with_suffix('.md'))
        _page['url'] = f'/{context}/{page}'
        _page['parent'] = str(Path(_page['url']).parent) + '/'
        _page['subpages'] = get_subpages(_page['url'])
        _page['has_content'] = True
        _page['content_path'] = str(path.relative_to(TEMPLATE_PATH))
    else:
        log.error(f'Page (/{context}/{page}) not found')
        abort(404)

    kwargs = {'page': _page}

    return render_template(_context['template'], **kwargs)
