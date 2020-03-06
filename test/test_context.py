import os
import yaml
import pytest
from pathlib import Path

PROJECT_PATH = Path(__file__).resolve().parent / "website"
os.chdir(PROJECT_PATH)

from staticpy import BASE_CONFIG, TEMPLATE_PATH
from staticpy.context import Context, PostContext, NoteContext
from website import app as site

app = site.app
site.build()

# Context (base class)
def test_context_constructor():
    expected = {
        "notes": {
            "source_path": PROJECT_PATH / "notes",
            "template": TEMPLATE_PATH / "note.html",
        },
        "posts": {
            "source_path": PROJECT_PATH / "posts",
            "template": TEMPLATE_PATH / "post.html",
        },
    }
    actual = {}

    for key, context_config in BASE_CONFIG["contexts"].items():
        context = Context(**context_config)
        actual[key] = {
            "source_path": context.source_path,
            "template": context.template,
        }

    assert expected == actual


def test_context_map():
    expected = {
        "posts/index.html": "posts/index.html",
        "posts/markdown-examples.html": "posts/markdown-examples.html",
        "posts/mathjax-examples.html": "posts/mathjax-examples.html",
        "posts/post1": "posts/post1",
        "posts/post1/index.html": "posts/post1/index.html",
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
        "posts/index.html": "posts/index.html",
        "posts/markdown-examples.html": "posts/markdown-examples.html",
        "posts/mathjax-examples.html": "posts/mathjax-examples.html",
        "posts/post1": "posts/post1",
        "posts/post1/index.html": "posts/post1/index.html",
    }

    context_config = BASE_CONFIG["contexts"]["posts"]
    context = Context(**context_config)
    actual = context.page_content_map

    print(expected)
    print(actual)
    assert expected == actual


def test_postcontext_serve():
    with app.test_client() as c:
        response = c.get("/posts/markdown-examples")
        print(response)
    assert False


# NoteContext
