from pathlib import Path
from shutil import copyfile, rmtree
from flask import (
    Flask,
    abort,
    redirect,
    request,
    render_template,
    send_from_directory,
    url_for,
)
from jinja2 import Markup
from . import BASE_CONFIG, TEMPLATE_PATH, STATIC_PATH, SITE_URL, log
from .config_handler import get_config
from .doc_builder import build_all
from .source_handler import Page, get_fpath, get_frontmatter
from .context import Context


app = Flask(__name__, template_folder=TEMPLATE_PATH, static_folder=STATIC_PATH)

if app.config["ENV"] == "production":
    SITE_URL = BASE_CONFIG["site_url"]
else:
    SITE_URL = "/"


########################
# META
########################
@app.context_processor
def global_var():
    def exists(file_or_path):
        """Check if the path exists in templates path."""
        fpath = TEMPLATE_PATH / get_fpath(file_or_path, resolve=False)
        return fpath.exists()

    def include_raw(fpath):
        return Markup(app.jinja_loader.get_source(app.jinja_env, fpath)[0])

    def new_url_for(endpoint, **kwargs):
        log.debug(f"Parsing {endpoint} {type(endpoint)}")
        ignore_prefix = ["#", "mailto"]
        should_ignore = map(lambda prefix: endpoint.startswith(prefix), ignore_prefix)

        if endpoint is None:
            url = ""
        elif any(should_ignore):
            # Handles external links
            url = endpoint
        elif endpoint[0] == "/":
            # Handles internal links
            url = SITE_URL + endpoint[1:]
        elif kwargs:
            # Handles flask-like url_for
            url = url_for(endpoint, **kwargs)
        else:
            # Give up and return input
            url = endpoint

        log.debug(f"Parsed as {url}")
        return url

    def get_current_page():
        return {}
        # url = request.path
        # return Page(url)

    var = dict(
        author=BASE_CONFIG["author"],
        page=get_current_page(),
        debug=app.debug,
        navbar=BASE_CONFIG["navbar"],
        exists=exists,
        include_raw=include_raw,
        url_for=new_url_for,
        site_url=SITE_URL,
        site_brand=BASE_CONFIG["site_brand"],
        site_title=BASE_CONFIG["site_title"],
        social_links=BASE_CONFIG["social_links"],
    )
    return var


@app.route("/favicon.ico")
def get_favicon():
    """Renders the favicon in /static/favicon.ico ."""
    return send_from_directory(STATIC_PATH, "favicon.ico")


########################
# MAIN
########################
@app.route("/<file>")
def get_root_page(file):
    """Renders root level pages located in `TEMPLATE_PATH`/<file>.

    This is often useful for the pages "about" and "contacts".
    """
    app.logger.debug(f"Root page requested")
    content_path = Path(file)
    if content_path.suffix == "":
        content_path = content_path.with_suffix(".html")

    if not (TEMPLATE_PATH / content_path).exists():
        app.logger.debug(f"Failed to serve root file {content_path}")
        abort(404)

    app.logger.debug(f"Serving root file {content_path}")
    return render_template(str(content_path))


@app.route(f"/<context>/")
@app.route(f"/<context>/<path:subpath>")
def get_page(context, subpath=None):
    """Most commonly used route to route pages belonging to a context.

    If URL is a HTML file (e.g., `/notes/file.html`), then it should have a HTML file in `TEMPLATE_PATH/<context>/<page>`. This file is imported to the context template specified in base configuration file `BASE_CONFIG` (e.g., `TEMPLATE_PATH/note.html`) and rendered.

    If URL is an index HTML file of the context (e.g., `/note/index.html`), the user is redirected to the context root URL (e.g., `/note`).

    If URL is an non-HTML file, the file itself is returned.

    If URL is a directory (e.g., `/notes/dir`), `TEMPLATE_PATH/notes/dir/index.html` is rendered if it exist otherwise an context template itself is rendered.
    """
    app.logger.debug(f"Context {context} page requested")
    page_url = request.path

    # Check if context is registered in config
    try:
        context_config = BASE_CONFIG["contexts"][context]
        context = Context(**context_config)
        app.logger.debug(f"Context found with map:\n\t{context.page_content_map}")
    except KeyError:
        app.logger.debug(f"Context {context} not found")
        abort(404)

    if subpath is None:
        # Render context root page
        content_path = context.get_content_path(page_url)
        if content_path is None:
            app.logger.debug(
                f"Cannot find content file in context associated with URL {page_url}."
            )
            abort(404)

        page = context.get_page(page_url)
        app.logger.debug(f"Serving context root page:\n\t{page}")
        return render_template(content_path, page=page)
    elif Path(subpath).suffix != "" and Path(subpath).suffix != ".html":
        # If URL is an non-HTML file, the file itself is returned.
        app.logger.debug(
            f"Non-HTML file found, serving {context.content_dir}/{subpath}"
        )
        return send_from_directory(context.content_dir, subpath)
    elif Path(subpath).name == "index.html":
        # If URL is context's index file redirect to context root URL
        app.logger.debug(
            f"Context root index file found, redirecting to {context.root_url}/{Path(subpath).parent}/"
        )
        return redirect(f"{context.root_url}/{Path(subpath).parent}/")
    else:
        # Otherwise render the content with context's template
        content_path = context.get_content_path(page_url)
        if content_path is None:
            app.logger.debug(
                f"Cannot find content file in context associated with URL {page_url}."
            )
            abort(404)

        page = context.get_page(page_url)
        app.logger.debug(f"Serving context page:\n\t{page}")
        return render_template(context.template, page=page)
