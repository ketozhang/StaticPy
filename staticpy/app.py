from pathlib import Path
from shutil import copyfile, rmtree
from flask import (
    Flask,
    abort,
    redirect,
    request,
    render_template,
    send_file,
    send_from_directory,
    url_for,
)
from jinja2 import Markup
from . import BASE_CONFIG, TEMPLATE_PATH, STATIC_PATH, SITE_URL, log
from .config_handler import get_config
from .doc_builder import build_all
from .source_handler import get_fpath, get_frontmatter, get_subpages
from .context import Context


app = Flask(__name__, template_folder=TEMPLATE_PATH, static_folder=STATIC_PATH)

if app.config["ENV"] == "production":
    SITE_URL = BASE_CONFIG["site_url"]
else:
    SITE_URL = "/"

print(f" * Serving StaticPy app to site URL {SITE_URL}")


########################
# META
########################
@app.context_processor
def global_var():
    # TODO SITE_URL best handled by a base config parser
    # site_url = SITE_URL if SITE_URL else "/"
    # if site_url[-1] != "/":
    #     site_url += "/"

    def exists(file_or_path):
        """Check if the path exists in templates path."""
        fpath = TEMPLATE_PATH / get_fpath(file_or_path, resolve=False)
        return fpath.exists()

    def include_raw(fpath):
        return Markup(app.jinja_loader.get_source(app.jinja_env, fpath)[0])

    def new_url_for(endpoint, **kwargs):
        log.info(f"Parsing {endpoint} {type(endpoint)}")
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

        log.info(f"Parsed as {url}")
        return url

    var = dict(
        author=BASE_CONFIG["author"],
        debug=app.debug,
        navbar=BASE_CONFIG["navbar"],
        exists=exists,
        include_raw=include_raw,
        url_for=new_url_for,
        site_url=SITE_URL,
        get_subpages=get_subpages,
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
    content_path = Path(file)
    if content_path.suffix == "":
        content_path = content_path.with_suffix(".html")

    if content_path.exists():
        return render_template(str(content_path))
    else:
        abort(404)


# @app.route(f"/<context>/<path:page>")
# def get_page(context, page):
#     """Routes all other page URLs. This supports both file and directory URL.

#     For files (e.g., /notes/file.html), the content of the markdown file
#     (e.g., /notes/file.md) is imported by the template.

#     For directories (e.g., /notes/dir/), if there exists a index file, the
#     directory is treated equivalent to the URL of the index file; otherwise,
#     the template is used with no content. Note that all directory URL have
#     trailing slashes; its left to the server to always redirect directory URL
#     without trailing slashes.

#     Context home pages (e.g., /note/index.html) are redirected to
#     `/<context>`.
#     """
#     log.info(f"Getting context: {context}, page: {page}")
#     path = TEMPLATE_PATH / context / page

#     # Got `/<context>/index.html`, redirect to context's homepage `/<context>`
#     if path.name == "index.html":
#         url = f"/{context}"
#         log.info(f"Redirecting to: {url}")
#         return redirect(f"/{context}")

#     # Attempt find the correct context
#     try:
#         _context = BASE_CONFIG["contexts"][context]
#         source_path = PROJECT_PATH / _context["source_path"]
#     except KeyError as e:
#         log.error(str(e) + f", when attempting with args get_page({context}, {page}).")

#     if (source_path / page).is_file() and path.suffix != ".html":
#         log.info(f"Fetching the file {str(source_path / page)}")
#         return send_file(str(source_path / page))

#     if page[-1] == "/":  # Handle directories
#         if not path.is_dir():
#             abort(404)
#         _page = get_frontmatter(source_path / page / "index.md")
#         _page["url"] = f"/{context}/{page}"
#         _page["parent"] = str(Path(_page["url"]).parent) + "/"
#         _page["subpages"] = get_subpages(_page["url"])
#         _page["has_content"] = (path / "index.html").exists() and (
#             path / "index.html"
#         ).stat().st_size > 1
#         _page["content_path"] = str((path / "index.html").relative_to(TEMPLATE_PATH))
#     elif path.with_suffix(".html").exists():  # Handle files
#         path = path.with_suffix(".html")
#         _page = get_frontmatter((source_path / page).with_suffix(".md"))
#         _page["url"] = f"/{context}/{page}"
#         _page["parent"] = str(Path(_page["url"]).parent) + "/"
#         _page["subpages"] = get_subpages(_page["url"])
#         _page["has_content"] = True
#         _page["content_path"] = str(path.relative_to(TEMPLATE_PATH))
#     else:
#         log.error(f"Page (/{context}/{page}) not found")
#         abort(404)

#     kwargs = {"page": _page}

#     return render_template(_context["template"], **kwargs)


@app.route(f"/<context>/<path:page_url>")
def get_page(context, page_url):
    """Most commonly used route to route pages belonging to a context.

    If URL is a file (e.g., `/notes/file.html`), then it should have a HTML file in `TEMPLATE_PATH/<context>/<page>`. This file is imported to the context template specified in base configuration file `BASE_CONFIG` (e.g., `TEMPLATE_PATH/note.html`) and rendered.

    If URL is a file is the index of the context (e.g., `/note/index.html`), the user is redirected to the context root URL (e.g., `/note`).

    If URL is a directory (e.g., `/notes/dir`), `TEMPLATE_PATH/notes/dir/index.html` is rendered if it exist otherwise an context template itself is rendered.
    """
    # Check if context is registered in config
    try:
        context_config = BASE_CONFIG["contexts"][context]
        context = Context(**context_config)
    except KeyError:
        abort(404)

    # If URL is context's index file redirect to context root URL
    if page_url == "index.html":
        return redirect(context.root_url)

    # All URL are route to a path in TEMPLATES_PATH
    content_path = context.get_content_path(page_url)

    # Handle files
    if content_path.is_file():
        # Render the page contents into the context's template
        return render_template(
            context.template, {"page": context.get_content_path(page_url)}
        )

    elif content_path.is_dir():
        raise NotImplementedError
    else:
        abort(404)

    return render_template(template_path, {"page": page_html_path})

    # Handle directory
