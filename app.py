#!/usr/bin/env python3
import sys
import logging
import frontmatter
import pypandoc as pandoc
from flask import Flask, render_template, url_for
# from flask_scss import Scss
from pathlib import Path
from shutil import rmtree
from src.config_handler import get_config

PROJECT_PATH = Path(__file__).resolve().parents[0]

# Load configurations
config = get_config()

# TODO: Choose either `site_url` or `root_url`.
ROOT_URL = Path(config['site_url']).resolve()
# BUILD_PATH = Path(config['build_path']).resolve()
TEMPLATES_PATH = Path(config['templates_path']).resolve()


app = Flask(__name__)
# Scss(app, static_dir='static', asset_dir='static')
log = app.logger


@app.context_processor
def global_var():
    var = dict(root_url=ROOT_URL)
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

    # Backup the build directory in templates
    backup = Path(TEMPLATES_PATH / f'{output_path.name}.bak')
    if output_path.exists():
        output_path.rename(backup)

    output_path.mkdir()
    try:  # Attempt to convert Markdown notes to HTML
        for note in source_path.glob('**/*.md'):
            parent = note.relative_to(source_path).parent  # /path/to/note/

            # mkdir /templates/notes/parent/
            if note.parent.stem != '':
                Path.mkdir(output_path / parent, exist_ok=True)

            outputfile = output_path / parent / (note.stem + '.html')
            log.debug(f"{note} >> {outputfile}")
            outputfile = md_to_html(note.resolve(), outputfile)
            assert outputfile.exists(), "The output file was not created."
        if backup.exists():
            rmtree(str(backup))
    except Exception as e:  # Recover backup when fails
        log.debug(e)
        rmtree(str(output_path))
        if backup.exists():
            backup.rename(output_path)


def build_all():
    for context in config['contexts'].values():
        build(context)


def get_all_notes():
    """Retrieve notes path relative to specified argument."""
    notes = TEMPLATES_PATH.glob('*/**/*.html')
    return [str(note.relative_to(TEMPLATES_PATH)) for note in notes]  # Ignores files at first level

############
# MAIN
############


@app.route('/')
def main():
    notes = get_all_notes()
    context = dict(notes=notes)
    return render_template('main.html', **context)


@app.route(f'/<context>/<path:note>')
def get_note(context, note):
    context = config['contexts'][context]
    source_path = PROJECT_PATH / context['source_path']
    output_path = TEMPLATES_PATH / context['source_path']

    # Get metadata and parse path
    if Path(note).suffix != '.html':
        metadata = frontmatter.load(source_path/(note + '.md'))
        note = output_path / (note + '.html')
    else:
        metadata = frontmatter.load(source_path/(note.replace('.html', '.md')))
        note = output_path / note

    # Resolve relative to template path
    # The note should now point to the actual HTML file while its served at /<path:note>
    # This decision was made to allow users to use any subdirectory url not just "domain.com/note"
    note = note.relative_to(TEMPLATES_PATH)
    log.info(f"Rendering {note}")

    context.update(dict(
        content_path=str(note),
        note=metadata
    ))
    return render_template('note.html', **context)


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 0:
        ROOT_URL = ''
        logging.basicConfig(level=logging.DEBUG)
        app.run(debug=True, port=8080)
    elif 'build' in args:
        build_all()
    else:
        raise ValueError("Invalid command. Use `python app.py ['build']`")
