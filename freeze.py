# Converts the Flask setup to build static files.
import sys
import logging
from flask_frozen import Freezer
from app import app, build_all, config, log, get_all_notes, PROJECT_PATH
from shutil import rmtree
freezer = Freezer(app)


@freezer.register_generator
def get_note():
    """
    A static URL generator for app.py::get_note.

    Yields
    -------
    args: dict
       The arguments of app.py::get_note.
    """
    for note_url in get_all_notes():
        note_url = note_url.split('/')
        context = note_url[0]
        note = '/'.join(note_url[1:])
        yield {'context': context, 'note': note}


def freeze():
    build_all()

    default_build_path = PROJECT_PATH / 'build'  # Default specified by Frozen-Flask
    build_path = PROJECT_PATH / config['build_path']
    backup = PROJECT_PATH / (build_path.name + '.bak')

    if build_path.exists():
        log.info(f"{build_path.name} -> {backup.name}")
        build_path.rename(backup)
    try:
        log.info("Building files...")
        freezer.freeze()

        log.info(f"{default_build_path.name} -> {build_path.name}")
        default_build_path.rename(build_path)

        if backup.exists():
            log.info(f"deleting {backup.name}")
            rmtree(str(backup))
    except Exception as e:
        log.error(e)
        if backup.exists():
            log.info(f"restoring {backup.name} -> {build_path.name}")
            backup.rename(build_path)
        if default_build_path.exists():
            log.info(f"deleting {default_build_path.name}")
            rmtree(str(default_build_path))


if __name__ == '__main__':
    args = sys.argv[1:]
    if 'debug' in args:
        app.debug = True
        logging.basicConfig(level=logging.DEBUG)

    freeze()
