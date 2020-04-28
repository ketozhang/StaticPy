import os
import yaml
import pytest
from pathlib import Path

PROJECT_PATH = Path(__file__).resolve().parent / "website"
os.chdir(PROJECT_PATH)
from .website import app as site

app = site.app


def test_serve():
    expected = {
        "/": 200,
        "/about": 200,
        "/empty": 200,
        "/posts/": 200,
        "/posts/markdown-examples/": 200,
        "/posts/mathjax-examples/": 200,
        "/posts/postdir/": 200,
        "/posts/postdir/index.html": 302,
        "/posts/empty_postdir/": 404,
        "/DOESNOTEXIST": 404,
        "/posts/DOESNOTEXIST": 404,
        "/notes/": 200,
        "/notes/Example_Notebook/": 200,
        "/notes/index.html": 302,
        "/notes/Example_Notebook/example/": 200,
        "/notes/Example_Notebook/example.png": 200,
        "/notes/Example_Notebook/sometext/": 200,
    }
    actual = {}

    for url in expected.keys():
        with app.test_client() as c:
            response = c.get(url)
            actual[url] = response.status_code
    assert expected == actual
