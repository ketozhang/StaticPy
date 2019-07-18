"""Handles all source for content and metadata needed by api request or Flask when generating templates"""
import os
import sys
import frontmatter
from pathlib import Path
from datetime import datetime
from .globals import *


def get_fpath(file_or_path, resolve=True):
    """Helper function for the arguments `file`, `path`, or `file_or_path` used
    below.

    Parses `file_or_path` that is either a string or pathlib.Path
    """
    if isinstance(file_or_path, str):
        fpath = Path(file_or_path)
    else:
        fpath = file_or_path

    if resolve:
        fpath = fpath.resolve()
    return fpath


def infer_title(fname):
    return fname.title().replace('_', ' ')



def get_frontmatter(file_or_path, last_updated=True, title=True):
    """Get parsed YAML frontmatter.

    Arguments
    ---------ath : str or pathlib.Path
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
        fpath = fpath / 'index.md'
    else:
        if fpath.suffix == '':
            fpath = fpath.with_suffix('.md')

    # Check exist
    if fpath.exists():
        fm = frontmatter.load(fpath).metadata

        # Add timestamp of most recent update to frontmatter
        if not ('last_updated' in fm):
            last_updated = datetime.fromtimestamp(os.path.getctime(fpath))
            # fm['date'] = last_updated.strftime('%Y-%m-%d %I:%M %p %Z')
            fm['last_updated'] = last_updated.isoformat()

        # Add title parsed from filename to frontmatter
        # Title ignores underscores and converts to title case.
        if not ('title' in fm):
            if fpath.stem == 'index':
                fm['title'] = infer_title(fpath.parent.stem)
            else:
                fm['title'] = infer_title(fpath.stem)

        return fm
    else:
        # Allow dir to not have index file
        # TODO: Deal with if fpath really do not exist,
        #       should we give fake frontmatter as well?
        fm = {}

        if fpath.stem == 'index':
            fm['title'] = infer_title(fpath.parent.stem)
        else:
            fm['title'] = infer_title(fpath.stem)

        return fm


def get_subpages(path):
    """Get immediate subpages of a path ignoring "index.*" pages.

    Parameters
    ----------
    path : str or pathlib.Path
        Directory relative to the project path or URL with leading slash.

    Returns
    -------
    pages : list
        a list of dictionaries containing metadata of a page including the URL and frontmatter.
    """
    if isinstance(path, str) and path[0] == '/':
        path = path[1:]

    path = get_fpath(path)

    if not path.is_dir():
        return {}

    pages = {}
    subpaths = []

    # Glob files
    extensions = ['md', 'html']
    for ext in extensions:
        subpaths.extend(path.glob(f'*.{ext}'))

    # Glob dirs
    # Unfortunately, Path.glob('*/) includes all files
    subpaths.extend([p for p in path.glob(f'*/')
                     if p.is_dir() and p.name[0] != '.'])

    for subpath in sorted(subpaths):
        if subpath.stem == 'index':
            continue
        subpath = subpath.resolve().relative_to(PROJECT_PATH)
        fm = get_frontmatter(subpath)

        if subpath.is_dir():
            url = '/' + str(subpath) + '/'
        else:
            url = '/' + str(subpath.with_suffix(''))

        pages[str(url)] = fm

    return pages
