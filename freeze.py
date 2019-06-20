# Converts the Flask setup to build static files.
import logging
import sys
import time
from flask_frozen import Freezer
from app import app, PROJECT_PATH, TEMPLATES_PATH, build_all, base_config, log, get_all_context_pages, get_root_page
from shutil import rmtree
freezer = Freezer(app)


@freezer.register_generator
def get_page():
    """
    A static URL generator for app.py::get_page.

    Yields
    -------
    args: dict
       The arguments of app.py::get_page.
    """
    for page_url in get_all_context_pages():
        page_url = page_url.split("/")
        context = page_url[0]
        page = "/".join(page_url[1:])
        yield {"context": context, "page": page}


@freezer.register_generator
def get_root_page():
    """
    A static URL generator for app.py::get_root_page.

    Yields
    -------
    args: dict
       The arguments of app.py::get_page.
    """
    for root_page_path in base_config['root_pages'].values():
        log.info(f"Converting {root_page_path} to static.")
        yield {"file": root_page_path}


def freeze():
    build_time = build_all()
    print(f"{'Template build time:':<30} {build_time:>6.2f} secs")

    start = time.time()
    default_build_path = PROJECT_PATH / "build"  # Default specified by Frozen-Flask
    build_path = PROJECT_PATH / base_config["build_path"]
    backup = PROJECT_PATH / (build_path.name + ".bak")

    if build_path.exists():
        log.info(f"{build_path.name} -> {backup.name}")
        build_path.rename(backup)
    try:
        log.info("Building files...")
        freezer.freeze()

        # Rename default build path to actual build path (e.g., build/ -> dev/)
        log.info(f"{default_build_path.name} -> {build_path.name}")
        default_build_path.rename(build_path)

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
        if default_build_path.exists():
            log.info(f"deleting {default_build_path.name}")
            rmtree(str(default_build_path))
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
