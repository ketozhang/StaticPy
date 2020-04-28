"""A starter app for StaticPy Minimal boilerplate."""
import sys
from flask import render_template
from staticpy import app, log, build_all, BASE_CONFIG, get_config

if app.debug:
    log.setLevel("DEBUG")

########################
# CUSTOM ROUTES
########################
@app.route("/")
def home():
    """Renders the home page."""
    return render_template("home.html")


def build():
    elapsed_time = build_all()
    print(f"Templates built in {elapsed_time:.2f} secs")


if __name__ == "__main__":
    args = sys.argv[1:]
    if "build" in args:
        build()
    else:
        raise ValueError("Invalid command. Use `python app.py [build]`")
