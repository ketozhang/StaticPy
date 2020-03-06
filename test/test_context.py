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


def test_context_map():
    expected = {
        "/posts/markdown-examples": "posts/markdown-examples.html",
        "/posts/mathjax-examples": "posts/mathjax-examples.html",
        "/posts/post1": "posts/post1",
        "/posts/post1/index.html": "posts/post1/index.html",
    }

    context_config = BASE_CONFIG["contexts"]["posts"]
    context = Context(**context_config)
    actual = context.page_content_map

    assert expected == actual


# PostContext
# def test_postcontext_constructor():
#     expected = BASE_CONFIG["contexts"]
#     actual = {}

#     for key, context_config in BASE_CONFIG["contexts"].items():
#         context = PostContext(**context_config)
#         actual[key] = {
#             "source_path": context.source_path,
#             "template": context.template,
#         }

#     assert expected == actual


def test_postcontext_map():
    expected = {
        "/posts/markdown-examples": "posts/markdown-examples.html",
        "/posts/mathjax-examples": "posts/mathjax-examples.html",
        "/posts/post1": "posts/post1",
        "/posts/post1/index.html": "posts/post1/index.html",
    }

    context_config = BASE_CONFIG["contexts"]["posts"]
    context = Context(**context_config)
    actual = context.page_content_map

    assert expected == actual


def test_postcontext_serve():
    expected = {
        "/posts/markdown-examples": 200,
        "/posts/mathjax-examples": 200,
        "/posts/post1": 200,
        "/posts/post1/index.html": 200,
        "/DOESNOTEXIST": 404,
        "/subdir/DOESNOTEXIST": 404,
    }
    actual = {}

    for url in expected.keys():
        with app.test_client() as c:
            response = c.get(url)
            actual[url] = response.status_code
    assert expected == actual


# NoteContext
