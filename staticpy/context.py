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
            source_path (str): Path to context. This is the same as the source path where its contents are stored.
            template (str): File path of the HTML template for contents relative to TEMPLATES_PATH.

        Attributes:
            source_path (pathlib.Path): See description of `path` in Args.
            template (pathlib.Path): Path to context's template.
            page_content_map (dict): Maps page URL (key) to content path (value) relative to `TEMPLATE_PATH`.

        """
        self.root_url = source_path
        self.source_path = PROJECT_PATH / source_path
        self.content_dir = TEMPLATE_PATH / source_path
        self.template = TEMPLATE_PATH / template

    @property
    def page_content_map(self):
        content_paths = [
            str(p.relative_to(TEMPLATE_PATH)) for p in self.content_dir.glob("**/*")
        ]
        self._page_content_map = {
            self.content_to_page(content_path): content_path
            for content_path in content_paths
        }

        return self._page_content_map

    def content_to_page(self, content_path):
        """Returns the page URL path given the content path relative to `TEMPLATE_PATH`

        Args:
         content_path (str): Content path relative to `TEMPLATE_PATH`

        Examples:
            ```
            <source_path>/page.html -> /<root_url>/page.html
            <source_path>/dir -> /<root_url>/dir
            <source_path>/dir/index.html -> /<root_url>/dir/index.html
            <source_path>/img.png -> /<root_url>/img.png
            ```
        """
        return content_path

    def page_to_content(self, page_url):
        """Returns the content path relative `TEMPLATE_PATH` given the page URL path relative to the context."""
        return self.page_content_map[page_url]

    # Alias
    get_content_path = page_to_content


class PostContext(Context):
    """A context fit for blogposts structure. The file structure may be nested but the virtual structure is single-level."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def content_to_page(self, content_path):
        """Returns the page URL path given the content path relative to `TEMPLATE_PATH`

        Converts a two-level nested structre into single-level. Assumes all first level directory has a second level HTML file `index.html`.

        Args:
            content_path (str): Content path relative to `TEMPLATE_PATH`

        Examples:
        ```
        <source_path>/post1.html -> /<root_url>/post1.html
        <source_path>/img1.png -> /<root_url>/img1.png
        <source_path>/post2/index.html -> /<root_url>/post2/index.html
        <source_path>/post2 -> /<root_url>/post2
        <source_path>/post2/img2.png -> /<root_url>/post2/img2.png
        ```
        """
        return content_path


class NoteContext(Context):
    pass
