import os
import sys
from pathlib import Path

PROJECT_PATH = Path(__file__).resolve().parent / "website"
TEMPLATE_PATH = PROJECT_PATH / "templates"
sys.path.insert(0, str(PROJECT_PATH))
os.chdir(PROJECT_PATH)


def test_freeze():
    from website import freeze

    expected = list(TEMPLATE_PATH.glob("**/*"))

    freeze.freeze()
    actual = list((PROJECT_PATH / "docs").glob("**/*"))

    expected == actual
