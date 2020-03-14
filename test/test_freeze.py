import os
import sys
from pathlib import Path
from time import perf_counter as timer

PROJECT_PATH = Path(__file__).resolve().parent / "website"
TEMPLATE_PATH = PROJECT_PATH / "templates"
sys.path.insert(0, str(PROJECT_PATH))
os.chdir(PROJECT_PATH)


def test_freeze():
    from website import freeze

    expected = list(TEMPLATE_PATH.glob("**/*"))

    start = timer()
    freeze.freeze()
    actual = list((PROJECT_PATH / "docs").glob("**/*"))

    print(f"Time Elapsed: {timer() - start}")
    assert expected == actual
