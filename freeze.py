# Converts the Flask setup to build static files.
import sys
import logging
from flask_frozen import Freezer
from app import app, build, log, get_all_notes, PROJECT_PATH
from shutil import rmtree
freezer = Freezer(app)


@freezer.register_generator
def get_note():
    for note in get_all_notes():
        yield {'note': note}


def freeze():
    app.debug = False
    app.testing = True
    build()
    freezer.freeze()


if __name__ == '__main__':
    args = sys.argv[1:]
    if 'debug' in args:
        app.debug = True
        logging.basicConfig(level=logging.DEBUG)
        
    docs = PROJECT_PATH / 'docs'
    default_build_path = PROJECT_PATH / 'build'
    backup = PROJECT_PATH / 'docs.bak'
    
    if docs.exists():
        log.debug(f"{docs.name} -> {backup.name}")
        docs.rename(backup)
    if default_build_path.exists():
        log.debug(f"deleting {default_build_path.name}")
        rmtree(str(default_build_path))
    try:
        log.debug("Building files...")
        freeze()
        
        log.debug(f"{default_build_path.name} -> {docs.name}")
        default_build_path.rename(docs)
        
        log.debug(f"deleting {backup.name}")
        rmtree(str(backup))
    except Exception as e:
        if backup.exists():
            log.debug(f"restoring {backup.name} -> {docs.name}")
            backup.rename(docs)