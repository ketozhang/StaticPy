import os
import yaml
import pytest
from pathlib import Path

PROJECT_PATH = Path(__file__).resolve().parent / "website"
os.chdir(PROJECT_PATH)

from staticpy import BASE_CONFIG, TEMPLATE_PATH, SITE_URL
from staticpy.context import Context, PostContext, NoteContext
from staticpy.source_handler import Page
from .website import app as site

app = site.app

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
            "content_dir": context.content_folder,
            "source_path": context.source_folder,
            "template": context.content_template,
        }

    print(expected)
    print(actual)
    assert expected == actual


def test_postcontext_map():
    expected = {
        "/posts/markdown-examples/": "posts/markdown-examples.html",
        "/posts/": "posts/index.html",
        "/posts/mathjax-examples/": "posts/mathjax-examples.html",
        "/posts/postdir/": "posts/postdir/index.html",
        "/posts/empty_post/": "posts/empty_post.html",
    }

    context_config = BASE_CONFIG["contexts"]["posts"]
    context = Context(**context_config)

    actual = context.page_content_map
    assert expected == actual


def test_context_source_files():
    context_config = BASE_CONFIG["contexts"]["notes"]
    context = Context(**context_config)

    expected = [
        "index.html",
        "Example_Notebook/sometext.md",
        "Example_Notebook/example.png",
        "Example_Notebook/example.md",
        "Example_Notebook/Section2/example.png",
        "Example_Notebook/Section2/example.md",
        "Example_Notebook/Section1/example.png",
        "Example_Notebook/Section1/example.md",
        "Deep_Notebook/example.png",
        "Deep_Notebook/example.md",
        "Deep_Notebook/Depth1/example.png",
        "Deep_Notebook/Depth1/example.md",
        "Deep_Notebook/Depth1/Depth2/example.png",
        "Deep_Notebook/Depth1/Depth2/example.md",
        "Deep_Notebook/Depth1/Depth2/Depth3/example.png",
        "Deep_Notebook/Depth1/Depth2/Depth3/example.md",
        "Deep_Notebook/Depth1/Depth2/Depth3/example.html",
    ]

    actual = context.source_files

    assert sorted(expected) == sorted(actual)


# def test_notecontext_map():
#     expected = {
#         "/notes/": "notes/index.html",
#         "/notes/Example_Notebook/example": "notes/Example_Notebook/example.html",
#         "/notes/Example_Notebook/": "notes/Example_Notebook/index.html",
#         "/notes/Example_Notebook/example.png": "notes/Example_Notebook/example.png",
#         "/notes/Example_Notebook/sometext": "notes/Example_Notebook/sometext.html",
#         "/notes/Example_Notebook/Section1/": "notes/Example_Notebook/Section1/index.html",
#         "/notes/Example_Notebook/Section1/example": "notes/Example_Notebook/Section1/example.html",
#         "/notes/Example_Notebook/Section1/example.png": "notes/Example_Notebook/Section1/example.png",
#         "/notes/Example_Notebook/Section2/": "notes/Example_Notebook/Section2/index.html",
#         "/notes/Example_Notebook/Section2/example": "notes/Example_Notebook/Section2/example.html",
#         "/notes/Example_Notebook/Section2/example.png": "notes/Example_Notebook/Section2/example.png",
#     }

#     context_config = BASE_CONFIG["contexts"]["notes"]
#     context = Context(**context_config)
#     actual = context.page_content_map

#     assert actual == expected


# def test_subpages():
#     expected = sorted(
#         [
#             "/notes/Example_Notebook/example/",
#             "/notes/Example_Notebook/sometext/",
#             "/notes/Example_Notebook/Section1/",
#             "/notes/Example_Notebook/Section2/",
#         ]
#     )

#     context_config = BASE_CONFIG["contexts"]["notes"]
#     context = Context(**context_config)
#     url = "/notes/Example_Notebook/"
#     page = context.get_page(url)

#     actual = sorted([subpage.url for subpage in page.subpages])

#     assert expected == actual


# def test_subpages_deep():
#     expected = sorted(
#         [
#             "/notes/Deep_Notebook/Depth1/",
#             "/notes/Deep_Notebook/Depth1/example/",
#             "/notes/Deep_Notebook/Depth1/Depth2/",
#             "/notes/Deep_Notebook/Depth1/Depth2/example/",
#             "/notes/Deep_Notebook/Depth1/Depth2/Depth3/",
#             "/notes/Deep_Notebook/Depth1/Depth2/Depth3/example/",
#             "/notes/Deep_Notebook/example/",
#         ]
#     )

#     context_config = BASE_CONFIG["contexts"]["notes"]
#     context = Context(**context_config)
#     url = "/notes/Deep_Notebook/"
#     page = context.get_page(url)
#     actual = []

#     def find_all_pages(page):
#         if len(page.subpages) == 0:
#             return

#         for subpage in page.subpages:
#             actual.append(subpage.url)
#             find_all_pages(subpage)

#     find_all_pages(page)

#     assert expected == actual
