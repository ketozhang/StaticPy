"""
Initializes the package first loading the configurations into global variables and
then forwarding the following API for the user:

* app
* build_all
* get_config
* log
* get_fpath, get_frontmatter, get_page, get_subpage
"""
import os
from pathlib import Path

# All relative paths must be relative to the CWD.
# User must make sure CWD is the root of their web project.
PROJECT_PATH = Path.cwd()
CONFIGS_PATH = os.environ.get("STATICPY_CONFIGS_PATH", PROJECT_PATH / "configs")

###
# LOAD CONFIG
###
import yaml


def get_config(filepath):
    """
    Reads YAML config file located at `filepath`.
    Returns config as dict if exists, otherwise throws exception.
    """

    # Validate Argument
    if isinstance(filepath, Path):
        config_path = filepath
    elif isinstance(filepath, str):
        if Path(filepath).is_absolute():
            config_path = Path(filepath)
        else:
            config_path = CONFIGS_PATH / filepath
    else:
        raise ValueError("Argument (0) `filepath` is not a valid file path.")

    # Read and return config file
    try:
        with open(config_path) as file:
            config = yaml.safe_load(file)
        return config
    except FileNotFoundError as e:
        raise FileNotFoundError(
            "Configuration file not found. Make sure to create one (default: `/path/to/project/configs/base.yaml`). \
             Use environment variable STATICPY_CONFIGS_PATH to change configs path."
        )


###
# GLOBAL VAR
###


def get_global_var(base_config):
    # Flask templates path
    template_path = PROJECT_PATH / base_config["template_path"]
    if not template_path.exists():
        raise FileNotFoundError(
            "Templates folder not found. Make sure to create one (default: /path/to/project/templates)."
        )

    # Web Static Path
    static_path = PROJECT_PATH / base_config["static_path"]
    if not static_path.exists():
        raise FileNotFoundError(
            "Static folder not found. Make sure to create one (default: /path/to/project/static)."
        )

    # Site URL
    # Will modify with trailing slash
    site_url = base_config["site_url"]
    if site_url[-1] != "/":
        site_url += "/"

    return template_path, static_path, site_url


BASE_CONFIG = get_config("base.yaml")
TEMPLATE_PATH, STATIC_PATH, SITE_URL = get_global_var(BASE_CONFIG)
DOC_EXTENSIONS = ["html", "md"]

###
# LOGGING
###
import logging

log = logging.getLogger(__name__)
c_format = logging.Formatter(
    "%(levelname)s:[%(module)s#%(funcName)s, line %(lineno)d]: %(message)s"
)
c_handler = logging.StreamHandler()
c_handler.setFormatter(c_format)
log.addHandler(c_handler)


###
# FORWARD APIs
###

from .app import app, build_all
