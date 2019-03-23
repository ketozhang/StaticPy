#!/usr/bin/env python3
import sys
import pypandoc as pandoc
from flask import Flask, render_template
from pathlib import Path
from shutil import rmtree
app = Flask(__name__)

PROJECT_PATH = Path(__file__).resolve().parents[0]
SOURCE_PATH = PROJECT_PATH / 'notes/'
TEMPLATES_PATH = PROJECT_PATH / 'templates/'
BUILD_PATH = TEMPLATES_PATH / 'notes/'


def get_fpath(file_or_path):
    if isinstance(file_or_path, str):
        fpath = Path(file_or_path).resolve()
    else:
        fpath = file_or_path.resolve()
    return fpath


def md_to_html(file_or_path, outputfile):
    fpath = get_fpath(file_or_path)
    outputfile = get_fpath(outputfile)
    pandoc.convert_file(str(fpath), 'html', outputfile=str(outputfile))
    return outputfile


# def get_outputfile(file_or_path):
#     fpath = get_fpath(file_or_path)


def build():
    if BUILD_PATH.exists():
        backup = Path(TEMPLATES_PATH / f'{BUILD_PATH.name}.bak')
        BUILD_PATH.rename(backup.name)
    BUILD_PATH.mkdir()
    try:
        for note in SOURCE_PATH.glob('**/*.md'):
            print(note, '>>', end='')
            parent = note.relative_to(SOURCE_PATH).parent  # /path/to/note/

            # mkdir /templates/notes/parent/
            print(parent)
            if note.parent.stem != '':
                print(BUILD_PATH / parent)
                Path.mkdir(BUILD_PATH / parent, exist_ok=True)

            outputfile = BUILD_PATH / parent / (note.stem + '.html')
            # print(outputfile)
            md_to_html(note.resolve(), outputfile)
    except Exception as e:
        print(e)
        rmtree(str(BUILD_PATH))
        BUILD_PATH.rename(BUILD_PATH.name)


@app.route('/')
def main():
    htmls = BUILD_PATH.glob('**/*.html')
    notes = [str(note.relative_to(TEMPLATES_PATH)) for note in htmls]
    context = dict(notes=notes)
    return render_template('main.html', **context)


@app.route('/example')
def example():
    return render_template('example.html')


@app.route('/notes/<path:note>')
def get_note(note):
    print(note)
    if Path(note).suffix != '.html':
        note += '.html'
    note = f'notes/{note}'
    context = dict(note=note)
    return render_template('note.html', **context)


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 0:
        app.run(debug=True, port=8080)
    if 'build' in args:
        build()
