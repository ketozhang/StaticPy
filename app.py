#!/usr/bin/env python3
import logging
import os
import sys
import time
from datetime import datetime
import frontmatter
import pypandoc as pandoc
from collections import OrderedDict
from flask import (Flask, render_template, url_for, send_from_directory,
        redirect)
from pathlib import Path
from shutil import rmtree, copyfile
from src.config_handler import get_config

# Load base_configurations
base_config = get_config()
PROJECT_PATH = Path(__file__).resolve().parents[0]
SITE_URL = base_config['site_url']
TEMPLATES_PATH = Path(base_config['templates_path']).resolve()

app = Flask(__name__)
log = app.logger

########################
# HELPER FUNCTIONS
########################


def get_fpath(file_or_path):
    if isinstance(file_or_path, str):
        fpath = Path(file_or_path).resolve()
    else:
        fpath = file_or_path.resolve()
    return fpath


def md_to_html(file_or_path, outputfile):
    fpath = get_fpath(file_or_path)
    outputfile = get_fpath(outputfile)
    pandoc.convert_file(str(fpath), 'html', outputfile=str(
        outputfile), extra_args=['--mathjax'])
    return outputfile


def build(context):
    """Converts the source directory (`source_path`) to a directory of html (`output_path`) outputted to the templates directory."""
    source_path = PROJECT_PATH / context['source_path']

    url = context['url']
    if url[0] == '/':
        url = url[1:]
    output_path = TEMPLATES_PATH / url

    # Backup the build directory in templates
    backup = Path(TEMPLATES_PATH / f'{output_path.name}.bak')
    if output_path.exists():
        log.info(f"{output_path.name} -> {backup.name}")
        output_path.rename(backup)

    output_path.mkdir()
    try:
        # Convert Markdown/HTML notes to HTML
        notes = list(source_path.glob('**/*.md')) + \
            list(source_path.glob('**/*.html'))
        for note in notes:
            parent = note.relative_to(source_path).parent  # /path/to/note/

            # mkdir /templates/notes/parent/
            if note.parent.stem != '':
                Path.mkdir(output_path / parent, exist_ok=True)

            outputfile = output_path / parent / (note.stem + '.html')
            log.debug(f"{note} >> {outputfile}")
            if note.suffix == '.md':
                outputfile = md_to_html(note.resolve(), outputfile)
            else:
                copyfile(str(note), str(outputfile))
            assert outputfile.exists(), "The output file was not created."

        # Copy over any raw HTML files
        for note in source_path.glob('**/*.html'):
            parent = note.relative_to(source_path).parent

        # Success, remove backup
        if backup.exists():
            rmtree(str(backup))
    except Exception as e:  # Recover backup when fails
        log.error(e)
        rmtree(str(output_path))
        if backup.exists():
            backup.rename(output_path)


def build_all():
    start = time.time()
    for context in base_config['contexts'].values():
        build(context)
    return time.time() - start


def get_all_context_pages():
    """Retrieve all pages accessible."""
    pages = TEMPLATES_PATH.glob('*/**/*.html')
    pages = [str(page.relative_to(TEMPLATES_PATH).as_posix())
             for page in pages]  # Ignores files at first level
    return pages


def get_frontmatter(file_or_path):
    """
    Arguments
    ---------
    file_or_path : str or pathlib.Path
        The path to the markdown file with frontmatter.
        Because frontmatter is loaded on request, the argument should be relative to project path.
        If URL is given, the path is assumed relative to project path with ".md" extension.

    Returns
    -------
    frontmatter: dict
        If `file_or_path` doesn't exist then return None.
        Otherwise, parse the frontmatter at `file_or_path` and return YAML data to dict.
    """
    if isinstance(file_or_path, str):
        fpath = Path(file_or_path)
    else:
        fpath = file_or_path

    # Parse path
    if fpath.suffix == '':
        fpath = fpath.with_suffix('.md')
    if not fpath.is_absolute():
        fpath = PROJECT_PATH / fpath

    # Check exist
    if not fpath.exists():
        return None

    fm = frontmatter.load(fpath).metadata

    # Add date to frontmatter if not specified
    if not ('date' in fm):
        last_updated = datetime.fromtimestamp(os.path.getctime(fpath))
        # fm['date'] = last_updated.strftime('%Y-%m-%d %I:%M %p %Z')
        fm['last_updated'] = last_updated.isoformat()

    return fm

def get_subpaths(path):
    """Get a list of the path's subpaths (child paths)."""
    if isinstance(path, str):
        path = Path(path)
    return [p.name + '/' for p in sorted(path.glob('*/'))]

########################
# META
########################


@app.context_processor
def global_var():
    # TODO SITE_URL best handled by a base_config parser
    site_url = SITE_URL if SITE_URL else '/'
    if site_url[-1] != '/':
        site_url += '/'

    var = dict(
        author=base_config['author'],
        site_url=site_url,
        site_brand=base_config['site_brand'],
        site_title=base_config['site_title'],
        debug=app.debug,
        social_links=base_config['social_links'],
        navbar=base_config['navbar']
    )
    return var


@app.route('/favicon.ico')
def favicon():
    """Renders the favicon in /static/favicon.ico ."""
    return send_from_directory('static', 'favicon.ico')


########################
# MAIN
########################
@app.route('/')
def home():
    """Renders the home page."""
    config = get_config('home')
    pages = get_all_context_pages()

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
    """
    Renders root level pages located in `TEMPLATES_PATH`/<file>.html .
    This is often useful for the pages "about" and "contacts".
    """
    fpath = Path(file) if isinstance(file, str) else file
    if fpath.suffix == "":
        fpath = fpath.with_suffix(".html")
    return render_template(str(file))

@app.route('/docs/')
def docs_home_page():
    """Renders the notes home page located in /documentations/index.html ."""
    context = base_config['contexts']['docs']
    return render_template(f"{context['url']}/index.html")

@app.route('/notes/')
def notes_home_page():
    """Renders the notes home page located in /notes/index.html ."""
    context = base_config['contexts']['notes']
    source_path = PROJECT_PATH / context['source_path']
    kwargs = dict(
        notebooks = get_subpaths(source_path),
        notebook_urls = get_subpaths(source_path)
    )
    return render_template(f"{context['url']}/index.html", **kwargs)


@app.route('/posts/')
def posts_home_page():
    """Renders the posts home page located in /notes/index.html ."""
    def get_all_posts():
        """
        Get post urls (path relative to `TEMPLATES_PATH`).

        Returns
        -------
        posts: list[str]
            A list of post urls as strings.
        """
        posts_path = TEMPLATES_PATH / 'posts'
        posts = posts_path.glob('**/[!index]*.html')
        posts = [str(post.relative_to(TEMPLATES_PATH).as_posix())
                 for post in posts]

        return posts

    posts = get_all_posts()
    posts_dict = OrderedDict()
    modified_times = []
    for post in posts:
        post_md_path = (PROJECT_PATH / post).with_suffix('.md')
        last_updated = datetime.fromtimestamp(os.path.getctime(post_md_path))
        modified_times.append(last_updated)
        fm = get_frontmatter(post_md_path)
        posts_dict[post] = fm
    sort_idx = sorted(range(len(modified_times)),
                      key=modified_times.__getitem__)[::-1]
    posts_dict = OrderedDict((list(posts_dict.items())[i]) for i in sort_idx)

    context = dict(
        posts=posts_dict
    )

    return render_template('posts/index.html', **context)


@app.route(f'/<context>/<path:page>')
def get_page(context, page='index.html'):
    log.info(f"Parsing /{context}/{page}")

    if page[-1] == '/':
        page = page[:-1] + '/index.html'

    # Attempt to find Flask route
    if page == 'index.html':
        try:  # If found redirect to /context/
            return redirect(url_for(f"{context}_home_page"))
        except Exception as e:  # TODO: Change to werkzeug BuildError
            log.debug(e)
            pass

    # Attempt finding the correct context
    try:
        context = base_config['contexts'][context]
    except KeyError as e:
        log.error(
            str(e) + f', when attempting with args get_page({context}, {page}).')

    source_path = PROJECT_PATH / context['source_path']

    url = context['url']
    if url[0] == '/':
        url = url[1:]
    output_path = TEMPLATES_PATH / url

    # If suffix is .html, then remove it with proper path
    if Path(page).suffix == '.html':
        page = str(Path(page).parent / Path(page).stem)

    fm = get_frontmatter(source_path/(str(page) + '.md'))
    page = output_path / (page + '.html')

    # Resolve relative to template path
    # The page should now point to the actual HTML file while its served at /<path:page>
    # This decision was made to allow users to use any subdirectory url not just "domain.com/page"
    page = page.relative_to(TEMPLATES_PATH).as_posix()
    log.info(f"Rendering {page}")

    context.update(dict(
        content_path=str(page),
        frontmatter=fm,
    ))

    if fm is None:
        return render_template(str(page), **context)
    else:  # Equivalent to checking if file is markdown.
        return render_template(context['template'], **context)


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 0:
        logging.basicConfig(level=logging.DEBUG)
        SITE_URL = ''
        app.run(debug=True, port=8080)
    elif 'build' in args:
        elapsed_time = build_all()
        print(f"Building templates finished in {elapsed_time:.2f}secs")
    else:
        raise ValueError("Invalid command. Use `python app.py ['build']`")
