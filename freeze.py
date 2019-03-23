from flask_frozen import Freezer
from app import app, get_all_notes, PROJECT_PATH
from shutil import rmtree
freezer = Freezer(app)


@freezer.register_generator
def get_note():
    for note in get_all_notes():
        yield {'note': note}


def freeze():
    app.debug = False
    app.testing = True
#     asset_manager.config['ASSETS_DEBUG'] = False
    freezer.freeze()


if __name__ == '__main__':
    docs = PROJECT_PATH / 'docs'
    build = PROJECT_PATH / 'build'
    backup = PROJECT_PATH / 'docs.bak'
    
    if docs.exists(): docs.rename(backup)
    if build.exists(): rmtree(str(build))
    try:
        freeze()
        build.rename(docs)
        rmtree(str(backup))
    except Exception as e:
        print(e)
        backup.rename(docs)
