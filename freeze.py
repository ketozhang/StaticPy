# Converts the Flask setup to build static files.
import logging
import sys
import time
from shutil import rmtree
from pathlib import Path
from flask_frozen import Freezer
from app import app
from staticpy import (build_all, log, get_fpath,
                      BASE_CONFIG, PROJECT_PATH)


freezer = Freezer(app)


########################
# HELPER FUNCTIONS
########################
def get_context_pages(context):
    """Returns a list of the context's page urls."""
    source_path = get_fpath(context['source_path']).relative_to(PROJECT_PATH)
    pages = []
    for page in list(source_path.rglob('*')):
        if page.name[0] == '.':
            # ignore hidden files
            pass
        elif page.is_dir():
            pages.append(str(page) + '/')
        elif page.suffix == '.md':
            pages.append(str(page.with_suffix('.html')))
        else:
            pages.append(str(page))
    return pages


def get_all_context_pages():
    """Retrieve all pages accessible for each context. This is determined if the HTML file exists in
    templates path.

    Ignores files that are at first level of templates path.
    """
    pages = []
    for context in BASE_CONFIG['contexts'].values():
        pages += get_context_pages(context)
    return pages


########################
# MAIN
########################
@freezer.register_generator
def get_page():
    """A static URL generator for app.py::get_page.

    Yields
    ------dict
       The arguments of app.py::get_page.
    """
    for page_url in get_all_context_pages():
        log.info(f"Freezing page: {page_url}")
        url_split = page_url.split("/")
        context = url_split[0]

        if url_split[1] == 'index.html':
            # For root pages, app.py::get_page will handle it
            # e.g., context/index.html
            page ='index.html'
        elif url_split[-1] == 'index.html':
            # e.g., context/.../page/index.html -> page := .../page/
            page = '/'.join(url_split[1:][:-1]) + '/'
        else:
            # e.g., context/.../page -> page := ../page
            page = '/'.join(url_split[1:])

        yield {"context": context, "page": page}


@freezer.register_generator
def get_root_page():
    """A static URL generator for app.py::get_root_page.

    Yields
    -------
    args: dict
       The arguments of app.py::get_page.
    """
    for root_page_path in BASE_CONFIG['root_pages'].values():
        log.info(f"Freezing root page: {root_page_path}.")
        yield {"file": root_page_path}


def freeze():
    build_time = build_all()
    print(f"{'Template build time:':<30} {build_time:>6.2f} secs")

    start = time.time()
    build_path = PROJECT_PATH / BASE_CONFIG["build_path"]
    backup = PROJECT_PATH / (build_path.name + ".bak")

    if build_path.exists():
        log.info(f"{build_path.name} -> {backup.name}")
        build_path.rename(backup)
    try:
        log.info("Building files...")
        app.config['FREEZER_DESTINATION'] = build_path
        freezer.freeze()

        if backup.exists():
            log.info(f"deleting {backup.name}")
            rmtree(str(backup))
        end = time.time()
        return end - start, build_time
    except Exception as e:
        log.error(e)
        if backup.exists():
            log.info(f"restoring {backup.name} -> {build_path.name}")
            backup.rename(build_path)
        if build_path.exists():
            log.info(f"deleting {build_path.name}")
            rmtree(str(build_path))
        return None


if __name__ == "__main__":
    args = sys.argv[1:]
    # if "debug" in args:
    if "debug" in args:
        app.debug = True
        logging.basicConfig(level=logging.DEBUG)
    elapsed_times = freeze()
    if elapsed_times is not None:
        print(
            f"{'Static convert time:':<30} {elapsed_times[0]:>6.2f} secs")
        print(
            f"{'Total time:':<30} {elapsed_times[0] + elapsed_times[1]:>6.2f} secs")
    else:
        print("Static conversion failed \nTry running `python freeze.py debug`")
