import os
import yaml
import pytest
from pathlib import Path

PROJECT_PATH = Path(__file__).resolve().parent / "website"
os.chdir(PROJECT_PATH)

#########
# Configurations
#########
from staticpy import get_config

with open(PROJECT_PATH / "configs" / "base.yaml") as file:
    config = yaml.safe_load(file)


def test_get_config_relative():
    actual = get_config("base.yaml")

    assert actual == config


def test_get_config_absolute():
    fpath = Path(PROJECT_PATH / "configs" / "base.yaml")
    actual = get_config(fpath)

    assert actual == config


def test_get_config_filenotfound():
    with pytest.raises(FileNotFoundError) as e:
        get_config("DOESNOTEXISTS")


#########
# Global Variables
#########
from staticpy import TEMPLATE_PATH, STATIC_PATH, SITE_URL


def test_template_path():
    expected = PROJECT_PATH / "templates"
    assert TEMPLATE_PATH == expected


def test_static_path():
    expected = PROJECT_PATH / "static"
    assert STATIC_PATH == expected


def test_site_url():
    expected = "https://ketozhang.github.io/StaticPy-Minimal-Boilerplate/"
    assert SITE_URL == expected


#####
# APP
#####


def test_app_init():
    from staticpy import app

    assert app.config != {}
