from flask_frozen import Freezer
from app import app, get_all_notes, PROJECT_PATH
freezer = Freezer(app)


@freezer.register_generator
def get_note():
    for note in get_all_notes():
        yield {'note': note}


def build():
    """ Builds this site.
    """
    print("Building website...")
    app.debug = False
    app.testing = True
#     asset_manager.config['ASSETS_DEBUG'] = False
    freezer.freeze()


if __name__ == '__main__':
    build()
    docs = PROJECT_PATH / 'build'
    docs.rename('docs')
