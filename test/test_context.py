import os
import yaml
import pytest
from pathlib import Path

PROJECT_PATH = Path(__file__).resolve().parent / "website"
os.chdir(PROJECT_PATH)

from staticpy import BASE_CONFIG, TEMPLATE_PATH, SITE_URL
from staticpy.context import Context, PostContext, NoteContext
from website import app as site

app = site.app
site.build()

# Context (base class)
def test_context_constructor():
    expected = {
        "notes": {
            "root_url": f"/notes",
            "content_dir": str(TEMPLATE_PATH / "notes"),
            "source_path": str(PROJECT_PATH / "notes"),
            "template": "note.html",
        },
        "posts": {
            "root_url": f"/posts",
            "content_dir": str(TEMPLATE_PATH / "posts"),
            "source_path": str(PROJECT_PATH / "posts"),
            "template": "post.html",
        },
    }
    actual = {}

    for key, context_config in BASE_CONFIG["contexts"].items():
        context = Context(**context_config)
        actual[key] = {
            "root_url": context.root_url,
            "content_dir": context.content_dir,
            "source_path": context.source_path,
            "template": context.template,
        }

    print(expected)
    print(actual)
    assert expected == actual


def test_context_serve():
    expected = {
        "/": 200,
        "/posts/": 200,
        "/posts/markdown-examples": 200,
        "/posts/mathjax-examples": 200,
        "/posts/postdir/": 200,
        "/posts/postdir/index.html": 302,
        "/posts/empty_postdir/": 404,
        "/DOESNOTEXIST": 404,
        "/posts/DOESNOTEXIST": 404,
        "/notes/": 200,
        "/notes/Example_Notebook/": 404,
        "/notes/index.html": 302,
        "/notes/Example_Notebook/example": 200,
        "/notes/Example_Notebook/example.png": 200,
        "/notes/Example_Notebook/sometext": 200,
    }
    actual = {}

    for url in expected.keys():
        with app.test_client() as c:
            response = c.get(url)
            actual[url] = response.status_code
    assert expected == actual


def test_postcontext_map():
    expected = {
        "/posts/markdown-examples": "posts/markdown-examples.html",
        "/posts/": "posts/index.html",
        "/posts/mathjax-examples": "posts/mathjax-examples.html",
        "/posts/postdir/": "posts/postdir/index.html",
        "/posts/empty_post": "posts/empty_post.html",
    }

    context_config = BASE_CONFIG["contexts"]["posts"]
    context = Context(**context_config)
    actual = context.page_content_map

    assert expected == actual


def test_notecontext_map():
    expected = {
        "/notes/": "notes/index.html",
        "/notes/Example_Notebook/example": "notes/Example_Notebook/example.html",
        "/notes/Example_Notebook/example.png": "notes/Example_Notebook/example.png",
        "/notes/Example_Notebook/sometext": "notes/Example_Notebook/sometext.html",
    }

    context_config = BASE_CONFIG["contexts"]["notes"]
    context = Context(**context_config)
    actual = context.page_content_map

    assert expected == actual
