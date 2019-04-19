#!/usr/bin/env python3
import os
import sys
import logging
import frontmatter
import pypandoc as pandoc
from collections import OrderedDict
from flask import Flask, render_template, url_for, send_from_directory
from pathlib import Path
from shutil import rmtree, copyfile
from src.config_handler import get_config

# Load base_configurations
base_config = get_config()
PROJECT_PATH = Path(__file__).resolve().parents[0]
# TODO: Choose either `site_url` or `root_url`.
ROOT_URL = base_config['site_url']
TEMPLATES_PATH = Path(base_config['templates_path']).resolve()

app = Flask(__name__)
log = app.logger


@app.context_processor
def global_var():
    # TODO ROOT_URL best handled by a base_config parser
    root_url = ROOT_URL if ROOT_URL else '/'
    if root_url[-1] != '/':
        root_url += '/'

    var = dict(
        root_url=root_url,
        links=base_config['links']
    )
    return var


def get_fpath(file_or_path):
    if isinstance(file_or_path, str):
        fpath = Path(file_or_path).resolve()
    else:
        fpath = file_or_path.resolve()
    return fpath


def md_to_html(file_or_path, outputfile):
    fpath = get_fpath(file_or_path)
    outputfile = get_fpath(outputfile)
    pandoc.convert_file(str(fpath), 'html', outputfile=str(
        outputfile), extra_args=['--mathjax'])
    return outputfile


def build(context):
    """Converts the source directory (`source_path`) to a directory of html (`output_path`) outputted to the templates directory."""
    source_path = PROJECT_PATH / context['source_path']
    output_path = TEMPLATES_PATH / context['source_path']
    print(f"{TEMPLATES_PATH / context['source_path']}")

    # Backup the build directory in templates
    backup = Path(TEMPLATES_PATH / f'{output_path.name}.bak')
    if output_path.exists():
        log.info(f"{output_path.name} -> {backup.name}")
        output_path.rename(backup)

    output_path.mkdir()
    try:
        # Convert Markdown/HTML notes to HTML
        notes = list(source_path.glob('**/*.md')) + \
            list(source_path.glob('**/*.html'))
        for note in notes:
            parent = note.relative_to(source_path).parent  # /path/to/note/

            # mkdir /templates/notes/parent/
            if note.parent.stem != '':
                Path.mkdir(output_path / parent, exist_ok=True)

            outputfile = output_path / parent / (note.stem + '.html')
            log.debug(f"{note} >> {outputfile}")
            if note.suffix == '.md':
                outputfile = md_to_html(note.resolve(), outputfile)
            else:
                copyfile(str(note), str(outputfile))
            assert outputfile.exists(), "The output file was not created."

        # Copy over any raw HTML files
        for note in source_path.glob('**/*.html'):
            parent = note.relative_to(source_path).parent

        # Success, remove backup
        if backup.exists():
            rmtree(str(backup))
    except Exception as e:  # Recover backup when fails
        log.error(e)
        rmtree(str(output_path))
        if backup.exists():
            backup.rename(output_path)


def build_all():
    for context in base_config['contexts'].values():
        build(context)


def get_all_notes():
    """Retrieve notes path relative to specified argument."""
    notes = TEMPLATES_PATH.glob('*/**/*.html')
    notes = [str(note.relative_to(TEMPLATES_PATH).as_posix())
             for note in notes]  # Ignores files at first level
    return notes


def get_frontmatter(file_or_path):
    """
    Arguments
    ---------
    file_or_path : str or pathlib.Path
        The path to the markdown file with frontmatter. 
        Because frontmatter is loaded on request, the argument should be relative to project path.
        If URL is given, the path is assumed relative to project path with ".md" extension.
    """
    if isinstance(file_or_path, str):
        fpath = Path(file_or_path)
    else:
        fpath = file_or_path

    if fpath.suffix == '':
        fpath = fpath.with_suffix('.md')
    if not fpath.is_absolute():
        fpath = PROJECT_PATH / fpath

    return frontmatter.load(fpath).metadata if fpath.exists() else None


############
# MAIN
############

@app.route('/')
def main():
    config = get_config('home')
    notes = get_all_notes()

    posts = config['posts']
    posts_dict = {}
    for post in posts:
        fm = get_frontmatter(post)
        posts_dict[post] = fm

    projects = config['projects']

    context = dict(
        notes=notes,
        posts=posts_dict,
        projects=projects
    )

    return render_template(config['template'], **context)

@app.route('/notes')
def notes_landing():
    return render_template('notes_landing.html')

@app.route('/posts')
def posts_landing():
    def get_all_posts():
        """
        Get post urls (path relative to `TEMPLATES_PATH`).

        Returns
        -------
        posts: list[str]
            A list of post urls as strings.
        """
        posts_path = TEMPLATES_PATH / 'posts'
        posts = posts_path.glob('**/[!index]*.html')
        posts = [str(post.relative_to(TEMPLATES_PATH).as_posix())
                 for post in posts]

        return posts

    posts = get_all_posts()
    posts_dict = OrderedDict()
    modified_times = []
    for post in posts:
        post_md_path = (PROJECT_PATH / post).with_suffix('.md')
        modified_times.append(os.path.getctime(post_md_path))
        fm = get_frontmatter(post_md_path)
        posts_dict[post] = fm
    sort_idx = sorted(range(len(modified_times)), key=modified_times.__getitem__)[::-1]
    print(posts_dict.items())
    posts_dict = OrderedDict((list(posts_dict.items())[i]) for i in sort_idx)

    context = dict(
        posts=posts_dict
    )

    return render_template('posts_landing.html', **context)


@app.route(f'/<context>')
@app.route(f'/<context>/<path:note>')
def get_note(context, note='index'):
    try:
        context = base_config['contexts'][context]
    except KeyError as e:
        log.error(
            str(e) + f', when attempting with args get_note({context}, {note}).')

    print(context, note)
    source_path = PROJECT_PATH / context['source_path']
    output_path = TEMPLATES_PATH / context['source_path']

    # Get metadata and parse path
    if Path(note).suffix == '.html':
        note = str(Path(note).parent / Path(note).stem)

    fm = get_frontmatter(source_path/(str(note) + '.md'))
    note = output_path / (note + '.html')

    # Resolve relative to template path
    # The note should now point to the actual HTML file while its served at /<path:note>
    # This decision was made to allow users to use any subdirectory url not just "domain.com/note"
    note = note.relative_to(TEMPLATES_PATH).as_posix()
    log.info(f"Rendering {note}")
    print(f"Rendering {note}")

    context.update(dict(
        content_path=str(note),
        frontmatter=fm,
    ))

    if fm is None:
        return render_template(str(note), **context)
    else:
        return render_template(context['template'], **context)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico')


if __name__ == '__main__':
    args = sys.argv[1:]
    logging.basicConfig(level=logging.DEBUG)
    if len(args) == 0:
        ROOT_URL = ''
        app.run(debug=True, port=8080)
    elif 'build' in args:
        build_all()
    else:
        raise ValueError("Invalid command. Use `python app.py ['build']`")
