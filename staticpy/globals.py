from pathlib import Path
from .config_handler import get_config


BASE_CONFIG = get_config()
PROJECT_PATH = Path(__file__).resolve().parents[1]
TEMPLATE_PATH = PROJECT_PATH / BASE_CONFIG['template_path']
STATIC_PATH = PROJECT_PATH / BASE_CONFIG['static_path']
SITE_URL = BASE_CONFIG['site_url']