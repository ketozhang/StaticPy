import time
from pathlib import Path
from shutil import rmtree
from flask_frozen import Freezer
from timeit import default_timer as timer
from . import BASE_CONFIG, PROJECT_PATH, app, build_all, log, Context

freezer = Freezer(app)


def get_all_context_pages():
    """Retrieve all pages accessible for each context. This is determined if the HTML file exists in
    templates path.

    Ignores files that are at first level of templates path.
    """
    pages = []
    for context_config in BASE_CONFIG["contexts"].values():
        context = Context(**context_config)
        pages += context.page_urls
    return pages


@freezer.register_generator
def get_page():
    """A static URL generator for app.py::get_page.

    Yields
    ------dict
       The arguments of app.py::get_page.
    """
    for page_url in get_all_context_pages():
        log.info(f"Freezing page: {page_url}")
        yield page_url


@freezer.register_generator
def get_root_page():
    """A static URL generator for app.py::get_root_page.

    Yields
    -------
    args: dict
       The arguments of app.py::get_page.
    """
    for root_page_path in BASE_CONFIG["root_pages"].values():
        log.info(f"Freezing root page: {root_page_path}.")
        yield {"file": root_page_path}


def freeze(skip_build=False):
    print("\n" + f"{' FREEZING ':=^80}")
    start = timer()

    build_path = PROJECT_PATH / BASE_CONFIG["build_path"]
    backup = PROJECT_PATH / (build_path.name + ".bak")

    if build_path.exists():
        log.info(f"{build_path.name} -> {backup.name}")
        build_path.rename(backup)
    try:
        app.config["FREEZER_DESTINATION"] = build_path
        freezer.old_freeze()

        if backup.exists():
            log.info(f"deleting {backup.name}")
            rmtree(str(backup))
        end = time.time()
        return timer() - start
    except Exception as e:
        log.exception(e)
        if build_path.exists():
            log.info(f"deleting {build_path.name}")
            rmtree(str(build_path))
        if backup.exists():
            log.info(f"restoring {backup.name} -> {build_path.name}")
            backup.rename(build_path)
        return


freezer.old_freeze = freezer.freeze
freezer.freeze = freeze
