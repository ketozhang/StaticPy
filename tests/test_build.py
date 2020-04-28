import os
import pytest
from pathlib import Path

PROJECT_PATH = Path(__file__).resolve().parent / "website"
os.chdir(PROJECT_PATH)


def test_all_context_build_to_template():
    from .website import app as site

    site.build()

    context_paths = ["notes/", "posts/"]

    expected = [
        "notes/Deep_Notebook",
        "notes/Deep_Notebook/Depth1",
        "notes/Deep_Notebook/Depth1/Depth2",
        "notes/Deep_Notebook/Depth1/Depth2/Depth3",
        "notes/Deep_Notebook/Depth1/Depth2/Depth3/example.html",
        "notes/Deep_Notebook/Depth1/Depth2/Depth3/example.png",
        "notes/Deep_Notebook/Depth1/Depth2/example.html",
        "notes/Deep_Notebook/Depth1/Depth2/example.png",
        "notes/Deep_Notebook/Depth1/example.html",
        "notes/Deep_Notebook/Depth1/example.png",
        "notes/Deep_Notebook/example.html",
        "notes/Deep_Notebook/example.png",
        "notes/Example_Notebook",
        "notes/Example_Notebook/Section1",
        "notes/Example_Notebook/Section1/example.html",
        "notes/Example_Notebook/Section1/example.png",
        "notes/Example_Notebook/Section2",
        "notes/Example_Notebook/Section2/example.html",
        "notes/Example_Notebook/Section2/example.png",
        "notes/Example_Notebook/example.html",
        "notes/Example_Notebook/example.png",
        "notes/Example_Notebook/sometext.html",
        "notes/index.html",
        "posts/empty_post.html",
        "posts/index.html",
        "posts/markdown-examples.html",
        "posts/mathjax-examples.html",
        "posts/postdir",
        "posts/postdir/index.html",
    ]

    actual = []
    for context_path in context_paths:
        content_paths = list(Path(PROJECT_PATH / context_path).glob("**/*"))
        for i, content_path in enumerate(content_paths):
            if str.lower(content_path.suffix) == ".md":
                content_paths[i] = content_path.with_suffix(".html")

        template_paths = list((PROJECT_PATH / "templates" / context_path).glob("**/*"))
        actual.extend(
            [str(p.relative_to(PROJECT_PATH / "templates")) for p in template_paths]
        )

    assert set(expected) == set(actual)


if __name__ == "__main__":
    test_all_context_build_to_template()
