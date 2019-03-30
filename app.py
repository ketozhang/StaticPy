#!/usr/bin/env python3
import sys
import logging
import frontmatter
import pypandoc as pandoc
from flask import Flask, render_template, url_for
from pathlib import Path
from shutil import rmtree, copyfile
from src.config_handler import get_config

PROJECT_PATH = Path(__file__).resolve().parents[0]

# Load configurations
config = get_config()

# TODO: Choose either `site_url` or `root_url`.
ROOT_URL = config['site_url']
# BUILD_PATH = Path(config['build_path']).resolve()
TEMPLATES_PATH = Path(config['templates_path']).resolve()

app = Flask(__name__)
log = app.logger


@app.context_processor
def global_var():
    var = dict(
        root_url=ROOT_URL if ROOT_URL else '/',
        links=config['links']
        )
    print(var)
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
    try:  
        # Convert Markdown/HTML notes to HTML
        notes = list(source_path.glob('**/*.md')) + list(source_path.glob('**/*.html'))
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
    for context in config['contexts'].values():
        build(context)


def get_all_notes():
    """Retrieve notes path relative to specified argument."""
    notes = TEMPLATES_PATH.glob('*/**/*.html')
    notes = [str(note.relative_to(TEMPLATES_PATH).as_posix()) for note in notes]  # Ignores files at first level
    return notes

############
# MAIN
############


@app.route('/')
def main():
    notes = get_all_notes()
    context = dict(notes=notes)
    return render_template('main.html', **context)


@app.route(f'/<context>')
@app.route(f'/<context>/<path:note>')
def get_note(context, note='index.html'):
    try:
        context = config['contexts'][context]
    except KeyError as e:
        log.error(str(e) + f', when attempting with args get_note({context}, {note}).')
    source_path = PROJECT_PATH / context['source_path']
    output_path = TEMPLATES_PATH / context['source_path']

    # Get metadata and parse path
    if Path(note).suffix != '.html':
        metadata = source_path/(note + '.md')
        note = output_path / (note + '.html')
    else:
        metadata = source_path/(note.replace('.html', '.md'))
        note = output_path / note
    if metadata.exists():
        metadata = frontmatter.load(metadata)
    else: 
        metadata = None

    # Resolve relative to template path
    # The note should now point to the actual HTML file while its served at /<path:note>
    # This decision was made to allow users to use any subdirectory url not just "domain.com/note"
    note = note.relative_to(TEMPLATES_PATH).as_posix()
    log.info(f"Rendering {note}")
    print(f"Rendering {note}")

    context.update(dict(
        content_path=str(note),
        note=metadata,
    ))

    if metadata is None:
        return render_template(str(note), **context)
    else:
        return render_template(context['template'], **context)


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
