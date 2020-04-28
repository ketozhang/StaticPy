"""
context_config = BASE_CONFIG["contexts"][context]
notes = Context(**context_config)
"""
from pathlib import Path
from . import PROJECT_PATH, TEMPLATE_PATH, SITE_URL
from .source_handler import Page


class Context:
    def __init__(self, source_folder=None, template=None, **kwargs):
        """A context is a root-level object that describes the structure of the context.

        Args:
            source_path (str): Path to context folder relative to `PROJECT_PATH`. Files inside this folder are called source files.
            template (str): File path of the HTML template for contents relative to TEMPLATES_PATH.

        Attributes:
            source_path (pathlib.Path): See description of `path` in Args.
            template (pathlib.Path): Path to context's template.
            page_content_map (dict): Maps page URL (key) to content path (value) relative to `TEMPLATE_PATH`.

        """
        self.root_url = f"/{source_folder}"
        self.source_folder = str(PROJECT_PATH / source_folder)
        self.content_folder = str(TEMPLATE_PATH / source_folder)
        self.content_template = template
        # Use pathlib.Path name convention
        self.ignore_paths = [str(Path(p)) for p in kwargs.pop("ignore_paths", [])]

        for k, v in kwargs.items():
            setattr(self, k, v)
        self._page_content_map = {}

    @property
    def page_content_map(self):
        # queue = [self.content_dir]

        # while queue:
        #     current_dir = queue.pop(0)
        #     current_content_paths = sorted(Path(current_dir).glob("*"))
        #     for content_path in current_content_paths:
        #         if content_path.is_dir():
        #             queue.append(content_path)

        #         content_path = content_path.relative_to(TEMPLATE_PATH)

        #         page_url = self.content_to_page(content_path)
        #         if page_url is None:
        #             # Handles directories, should be overwritten if /path/to/dir/index.html exists
        #             self._page_content_map[
        #                 f"/{content_path}/"
        #             ] = f"{content_path}/index.html"
        #         else:
        #             self._page_content_map[page_url] = content_path

        # List of path to contents relative to the TEMPLATE_PATH
        content_paths = [
            str(p.relative_to(TEMPLATE_PATH))
            for p in sorted(Path(self.content_folder).glob("**/*"))
        ]

        self._page_content_map = {}
        for content_path in content_paths:
            page_url = self.content_to_page_url(content_path)
            if Path(content_path).suffix == "":
                # Handles directories, should be overwritten if /path/to/dir/index.html exists
                self._page_content_map[page_url] = str(
                    Path(content_path) / "index.html"
                )
            else:
                self._page_content_map[page_url] = content_path

        return self._page_content_map

    @property
    def page_urls(self):
        return self.page_content_map.keys()

    @property
    def source_files(self):
        """Return a list of source files excluding ignored files. The source files are relative to `self.source_path`"""

        self._source_files = []

        def is_ignored(path):
            parents = [str(p) for p in path.parents]
            parent_is_ignored = bool(set() & set(self.ignore_paths))
            itself_is_ignored = str(path) in self.ignore_paths

            return parent_is_ignored or itself_is_ignored

        def dfs(path):
            # If path is ignored, stop
            if is_ignored(path.relative_to(self.source_folder)):
                return

            # If path is a file, record it
            if path.is_file():
                self._source_files.append(str(path.relative_to(self.source_folder)))

            # Search path's child
            for subpath in path.glob("*"):
                dfs(subpath)

        dfs(Path(self.source_folder))
        return self._source_files

        # queue = [Path(self.source_path)]
        # while len(queue) > 0:
        #     current_path = queue.pop(0)
        #     subpaths = current_path.glob("*")
        #     for subpath in subpaths:
        #         if str(subpath.relative_to(subpath.parent)) not in self.ignore_paths:
        #             queue.append(subpath)
        #             self._source_files.append(str(subpath.relative_to(PROJECT_PATH)))

    def __repr__(self):
        s = f"<Context: url={self.root_url}, content_template={self.content_template}>"
        return s

    def __str__(self):
        return self.__repr__()

    def get_page(self, url):
        """Returns Page searched by its URL"""
        content_path = self.get_content_path(url)
        return Page(url, content_path, self)

    def content_to_page_url(self, content_path):
        """Returns the page URL path given the content path relative to `TEMPLATE_PATH`

        Args:
         content_path (str): Content path relative to `TEMPLATE_PATH`
        """
        content_path = Path(content_path)

        if content_path.suffix == "":
            # Folders itself have no content so an empty "index.html" is referenced
            return f"/{content_path}/"
        elif content_path.suffix == ".html":
            if content_path.name == "index.html":
                # Index files maps to its parent directory (e.g., /dir/)
                return f"/{content_path.parent}/"
            else:
                # HTML files maps to itself without suffix (e.g., /page/)
                return f"/{content_path.with_suffix('')}/"
        else:
            # Non-HTML files maps to itself (e.g., /img.png)
            return f"/{content_path}"

    def page_to_content(self, page_url):
        """Returns the content path relative `TEMPLATE_PATH` given the page URL path relative to the context if exists otherwise return None."""
        return self.page_content_map.get(page_url, None)

    def get_content_path(self, *args, **kwargs):
        """An alias to self.page_to_content"""
        return self.page_to_content(*args, **kwargs)


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
        return super().get_content_path(self, content_path)


class NoteContext(Context):
    pass
