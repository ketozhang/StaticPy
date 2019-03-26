#!/usr/bin/env python3
import sys
import pypandoc as pandoc
import logging
import frontmatter
from flask import Flask, render_template, url_for
from pathlib import Path
from shutil import rmtree

PROJECT_PATH = Path(__file__).resolve().parents[0]
SOURCE_PATH = PROJECT_PATH / 'notes/'
TEMPLATES_PATH = PROJECT_PATH / 'templates/'
BUILD_PATH = TEMPLATES_PATH / 'notes/'
ROOT_URL = 'https://ketozhang.github.io/notebook'

app = Flask(__name__)
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
    pandoc.convert_file(str(fpath), 'html', outputfile=str(outputfile), extra_args=['--mathjax'])
    return outputfile


def build():
    """Converts the notes directory (`SOURCE_PATH`) to a directory of html (`BUILD_PATH`) outputted to the templates directory."""
    # Backup the build directory in templates
    backup = Path(TEMPLATES_PATH / f'{BUILD_PATH.name}.bak')
    if BUILD_PATH.exists():
        BUILD_PATH.rename(backup)

    BUILD_PATH.mkdir()
    try:  # Attempt to convert Markdown notes to HTML
        for note in SOURCE_PATH.glob('**/*.md'):
            parent = note.relative_to(SOURCE_PATH).parent  # /path/to/note/

            # mkdir /templates/notes/parent/
            if note.parent.stem != '':
                Path.mkdir(BUILD_PATH / parent, exist_ok=True)

            outputfile = BUILD_PATH / parent / (note.stem + '.html')
            log.debug(f"{note} >> {outputfile}")
            outputfile = md_to_html(note.resolve(), outputfile)
            assert outputfile.exists(), "The output file was not created."
        if backup.exists():
            rmtree(str(backup))
    except Exception as e:  # Recover backup when fails
        log.debug(e)
        rmtree(str(BUILD_PATH))
        if backup.exists():
            backup.rename(BUILD_PATH)


def get_all_notes(relative_to=BUILD_PATH):
    htmls = BUILD_PATH.glob('**/*.html')
    notes = [str(note.relative_to(relative_to)) for note in htmls]
    return notes


@app.route('/')
def main():
    notes = get_all_notes(relative_to=TEMPLATES_PATH)
    context = dict(notes=notes)
    return render_template('main.html', **context)


@app.route('/notes/<path:note>')
def get_note(note):

    # Get metadata and parse path
    if Path(note).suffix != '.html':
        metadata = frontmatter.load(SOURCE_PATH/(note + '.md'))
        note = BUILD_PATH / (note + '.html')
    else:
        metadata = frontmatter.load(SOURCE_PATH/(note.replace('.html', '.md')))
        note = BUILD_PATH / note

    # Resolve relative to template path
    # The note should now point to the actual HTML file while its served at /<path:note>
    # This decision was made to allow users to use any subdirectory url not just "domain.com/note"
    note = note.relative_to(TEMPLATES_PATH)
    log.info(f"Rendering {note}")
    
    context = dict(
        content_path=str(note),
        note=metadata
        )
    return render_template('note.html', **context)


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 0:
        ROOT_URL = ''
        logging.basicConfig(level=logging.DEBUG)
        app.run(debug=True, port=8080)
    elif 'build' in args:
        build()
    else:
        raise ValueError("Invalid command. Use `python app.py ['build']`")
