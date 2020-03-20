"""
Initializes the package first loading the configurations into global variables and
then forwarding the following API for the user:

* app
* build_all
* get_config
* log
* get_fpath, get_frontmatter, get_page, get_subpage
"""
import logging
import os
from pathlib import Path

import yaml
from flask import Flask

#########
# LOGGING
#########
log = logging.getLogger(__name__)
c_format = logging.Formatter(
    "%(levelname)s:[%(module)s#%(funcName)s, line %(lineno)d]: %(message)s"
)
c_handler = logging.StreamHandler()
c_handler.setFormatter(c_format)
log.addHandler(c_handler)


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


def get_configs_path():
    configs_path = os.environ.get("STATICPY_CONFIGS_PATH", PROJECT_PATH / "configs")
    if not configs_path.exists():
        raise FileNotFoundError(
            "Configs folder not found. Make sure to create one (default: /path/to/project/templates) or set environment variable STATICPY_CONFIGS_PATH."
        )
    return configs_path


def get_template_path(base_config):
    # Flask templates path
    template_path = PROJECT_PATH / base_config["template_path"]
    if not template_path.exists():
        raise FileNotFoundError(
            "Templates folder not found. Make sure to create one (default: /path/to/project/templates)."
        )
    return template_path


def get_static_path(base_config):
    # Web Static Path
    static_path = PROJECT_PATH / base_config["static_path"]
    if not static_path.exists():
        raise FileNotFoundError(
            "Static folder not found. Make sure to create one (default: /path/to/project/static)."
        )

    return static_path


def get_site_url(base_config):
    # Site URL
    # Will modify with trailing slash
    site_url = base_config["site_url"]
    if site_url[-1] != "/":
        site_url += "/"

    return site_url


##################
# GLOBAL VARIABLES
##################
# All relative paths must be relative to the CWD.
# User must make sure CWD is the root of their web project.
PROJECT_PATH = Path.cwd()
CONFIGS_PATH = get_configs_path()
BASE_CONFIG = get_config("base.yaml")
TEMPLATE_PATH = get_template_path(BASE_CONFIG)
STATIC_PATH = get_static_path(BASE_CONFIG)
SITE_URL = get_site_url(BASE_CONFIG)
DOC_EXTENSIONS = ["html", "md"]
from .context import Context

CONTEXTS = {
    context_name: Context(**config)
    for context_name, config in BASE_CONFIG["contexts"].items()
}

################
# INITIALIZATION
################
from .doc_builder import build_all

app = Flask(__name__, template_folder=TEMPLATE_PATH, static_folder=STATIC_PATH)

if app.config["ENV"] == "production":
    SITE_URL = BASE_CONFIG["site_url"]
else:
    SITE_URL = "/"

from . import routes
