"""Handles all source for content and metadata needed by api request or Flask when generating templates"""
import os
import sys
import frontmatter
from pathlib import Path
from datetime import datetime
from .globals import *
from .page import Page

DOC_EXTENSIONS = ["html", "md"]


def get_fpath(file_or_path, resolve=True):
    """
    Parse `file_or_path` as string or pathlib.Path
    and returns pathlib.Path.
    """
    if isinstance(file_or_path, str):
        fpath = Path(file_or_path)
    else:
        fpath = file_or_path

    if resolve:
        fpath = fpath.absolute()
    return fpath


def infer_title(fname):
    return fname.title().replace("_", " ")


def get_frontmatter(file_or_path, last_updated=True, title=True):
    """Get parsed YAML frontmatter.

    Arguments
    ---------
    file_or_path : str or pathlib.Path
        If path to file, then the path should be to a markdown file. ".md" extension is assumed if missing.
        If path to directory, then the path should contain index.md.
        Because frontmatter is loaded on request, the argument should always be relative to project path.
    last_updated : bool
        If True, the frontmatter will be set the key "last_updated" with the timestamp of `file_or_path`'s
        most recent update. If the key exists, skip.
    title: bool
        If True, the key "Title" will be added to the frontmatter with value parsed from `file_or_path`'s name.
        If the key exists, skip.

    Returns
    -------
    frontmatter: dict
        If `file_or_path` doesn't exist or frontmatter is can't be found then return empty dict.
        Otherwise, return a parse of the frontmatter YAML data to dict.
    """
    fpath = PROJECT_PATH / get_fpath(file_or_path)

    # Parse path
    if fpath.is_dir():
        fpath = fpath / "index.md"
    else:
        if fpath.suffix == "":
            fpath = fpath.with_suffix(".md")

    if fpath.suffix[1:] not in DOC_EXTENSIONS:
        raise ValueError(
            f"Argument `file_or_path` must be refer to a file type {DOC_EXTENSIONS}"
        )

    # Check exist
    if fpath.exists():
        fm = frontmatter.load(fpath).metadata

        # Add timestamp of most recent update to frontmatter
        if not ("last_updated" in fm):
            last_updated = datetime.fromtimestamp(os.path.getctime(fpath))
            # fm['date'] = last_updated.strftime('%Y-%m-%d %I:%M %p %Z')
            fm["last_updated"] = last_updated.isoformat()

        # Add title parsed from filename to frontmatter
        # Title ignores underscores and converts to title case.
        if not ("title" in fm):
            if fpath.stem == "index":
                fm["title"] = infer_title(fpath.parent.stem)
            else:
                fm["title"] = infer_title(fpath.stem)

        return fm
    else:
        # Allow dir to not have index file
        # TODO: Deal with if fpath really do not exist,
        #       should we give fake frontmatter as well?
        fm = {}

        if fpath.stem == "index":
            fm["title"] = infer_title(fpath.parent.stem)
        else:
            fm["title"] = infer_title(fpath.stem)

        return fm


def get_page(path):
    """
    Parameters
    ----------
    path : str or pathlib.Path
        File path or URL relative to the project path or URL with leading slash.
    Returns
    -------
    pages : Page
    """

    # Remove trailing slash for file system
    if isinstance(path, str) and path[0] == "/":
        path = path[1:]

    path = get_fpath(path)

    if path.is_file() and path.suffix in DOC_EXTENSIONS:
        url = "/" + str(path.absolute().relative_to(PROJECT_PATH).stem)
    elif any([path.with_suffix(f".{ext}") for ext in DOC_EXTENSIONS]):
        url = "/" + str(path.absolute().relative_to(PROJECT_PATH))
    else:
        raise ValueError(
            f"Argument `path` does not point to any supporting files of extension: {DOC_EXTENSIONS}"
        )

    frontmatter = get_frontmatter(str(path))
    return Page(url, **frontmatter)


def get_subpages(path, recursive=True):
    # TODO: Allow recursion
    """Get immediate subpages of a path ignoring "index.*" pages.

    Parameters
    ----------
    path : str or pathlib.Path
        Directory path or URL relative to the project path or URL with leading slash.
        If `/path/to/project/context/page`, `path` should be `/context/page`.
        This follows conventions for URL paths as `/context/page` is the URL
        to the page.

        .. warning::
            Using `index.html` will always return an empty dictionary. Instead
            use the `index.html` parent path.

    Returns
    -------
    pages : list
        A list of Page object.
    """
    # Remove trailing slash for file system
    if isinstance(path, str) and path[0] == "/":
        path = path[1:]

    path = get_fpath(path)

    # A file does not have subpages
    if not path.is_dir():
        return {}

    subpages = []
    subpaths = []

    # Glob all Markdown and HTML files to subpaths
    for ext in DOC_EXTENSIONS:
        subpaths.extend(path.glob(f"*.{ext}"))

    # Glob all subdirectories
    subfiles_and_path = list(path.glob("*/"))
    subpaths.extend([d for d in subfiles_and_path if d.is_dir()])

    # Unfortunately, Path.glob('*/) includes all files
    # subpaths.extend([p for p in path.glob(f"**/") if p.is_dir() and p.name[0] != "."])

    for subpath in sorted(subpaths):
        # ignore hidden paths, index.html, and index.md
        is_hidden = str(subpath)[0] == "."
        is_index = subpath.name in [f"index.{ext}" for ext in DOC_EXTENSIONS]
        if is_hidden or is_index:
            continue

        # Convert subpath to URL
        subpath = subpath.absolute().relative_to(PROJECT_PATH)
        frontmatter = get_frontmatter(str(subpath))

        if subpath.is_dir():
            # directory URL ends in trailing slahses
            url = "/" + str(subpath) + "/"

            # # Recursion: Get subpages of directory
            if recursive:
                subsubpages = get_subpages(url)
            else:
                subsubpages = None
        else:
            # file URL does not
            url = "/" + str(subpath.with_suffix(""))
            subsubpages = []

        subpage = Page(url, subpages=subsubpages, **frontmatter)
        subpages.append(subpage)

    return subpages

