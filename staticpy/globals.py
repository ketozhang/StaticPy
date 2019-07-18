from pathlib import Path
from .config_handler import get_config, PROJECT_PATH


BASE_CONFIG = get_config()
TEMPLATE_PATH = PROJECT_PATH / BASE_CONFIG['template_path']
STATIC_PATH = PROJECT_PATH / BASE_CONFIG['static_path']
SITE_URL = BASE_CONFIG['site_url']