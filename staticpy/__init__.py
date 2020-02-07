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

    if isinstance(filepath, Path):
        config_path = filepath
    elif isinstance(filepath, str):
        if Path(filepath).is_absolute():
            config_path = Path(filepath)
        else:
            config_path = CONFIGS_PATH / filepath
    else:
        raise ValueError("Argument (0) `filepath` is not a valid file path.")

    try:
        with open(config_path) as file:
            config = yaml.safe_load(file)
        return config
    except FileNotFoundError as e:
        raise e


###
# GLOBAL VAR
###

BASE_CONFIG = get_config("base.yaml")
TEMPLATE_PATH = PROJECT_PATH / BASE_CONFIG["template_path"]
STATIC_PATH = PROJECT_PATH / BASE_CONFIG["static_path"]
SITE_URL = BASE_CONFIG["site_url"]


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
from .source_handler import (
    get_fpath,
    get_frontmatter,
    get_page,
    get_subpages,
)
