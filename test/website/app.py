"""A starter app for StaticPy Minimal boilerplate."""
import sys
from flask import render_template
from staticpy import app, log, build_all, BASE_CONFIG, get_config

# if app.debug:
#     log.setLevel("DEBUG")
# else:
#     log.setlevel("WARNING")

########################
# CUSTOM ROUTES
########################
@app.route("/")
def home():
    """Renders the home page."""
    return render_template("home.html")


@app.route("/notes/")
def notes_page():
    """Renders the notes page which lists links to all notes."""
    context = BASE_CONFIG["contexts"]["notes"]
    return render_template("notes/index.html", **context)


@app.route("/posts/")
def posts_page():
    """Renders the posts page which lists links to all posts."""
    context = BASE_CONFIG["contexts"]["posts"]
    return render_template("posts/index.html", **context)


def build():
    elapsed_time = build_all()
    print(f"Building templates finished in {elapsed_time:.2f}secs")

if __name__ == "__main__":
    args = sys.argv[1:]
    if "build" in args:
        build()
    else:
        raise ValueError("Invalid command. Use `python app.py [build]`")
