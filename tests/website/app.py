"""A starter app for StaticPy Minimal boilerplate."""
import sys
from flask import render_template
from staticpy import app, log, freezer, build_all, BASE_CONFIG, get_config

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

    times = []

    if "build" in args:
        build_time = build_all()

        if build_time is not None:
            print(f"{'Build time:':<30} {build_time:.2f} secs")
            times.append(build_time)

    if "freeze" in args:
        freeze_time = freezer.freeze()
        if freeze_time is not None:
            print(f"{'Static convert time:':<30} {freeze_time:.2f} secs")
            times.append(build_time)

        else:
            print(
                "Static conversion failed \nTry setting `FLASK_ENV=development` for debugging"
            )

    if times:
        print(f"\n{'':=^80}")
        print(f"{'Total time:':<30} {sum(times) :.2f} secs\n")
