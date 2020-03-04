"""
context_config = BASE_CONFIG["contexts"][context]
notes = Context(**context_config)
"""
from pathlib import Path
from . import PROJECT_PATH, TEMPLATE_PATH


class Context:
    def __init__(self, source_path, template, **kwargs):
        """A context is a root-level object that describes the structure of the context.

        Args:
            source_path (str): Path to context. This is the same as its source path where its contents are stored.
            template (str): File path of the HTML template for contents relative to TEMPLATES_PATH.

        Attributes:
            source_path (pathlib.Path): See description of `path` in Args.
            template (pathlib.Path):
        """
        self.source_path = PROJECT_PATH / source_path
        self.template = TEMPLATE_PATH / template


class PostContext(Context):
    """A context fit for blogposts structure. The file structure may be nested but the virtual structure is single-level."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class NoteContext(Context):
    pass
