import os
import pytest
from pathlib import Path

PROJECT_PATH = Path(__file__).resolve().parent / "website"
os.chdir(PROJECT_PATH)


def test_all_context_build_to_template():
    from website import app as site

    site.build()

    context_paths = ["notes/", "posts/"]

    expected = []
    actual = []
    for context_path in context_paths:
        content_paths = list(Path(PROJECT_PATH / context_path).glob("**/*"))
        for i, content_path in enumerate(content_paths):
            if str.lower(content_path.suffix) == ".md":
                content_paths[i] = content_path.with_suffix(".html")
        expected.extend([p.relative_to(PROJECT_PATH) for p in content_paths])

        template_paths = list((PROJECT_PATH / "templates" / context_path).glob("**/*"))
        actual.extend(
            [p.relative_to(PROJECT_PATH / "templates") for p in template_paths]
        )

    assert set(actual) == set(expected)


if __name__ == "__main__":
    test_all_context_build_to_template()
