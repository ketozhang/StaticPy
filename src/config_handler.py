import yaml
from pathlib import Path
PROJECT_PATH = Path(__file__).resolve().parents[1]

config = PROJECT_PATH / 'config.yaml'
assert config.exists(), "`config.yaml` is required. Make one even if it's empty."

def get_config(file_or_path=config):
    if isinstance(file_or_path, Path):
        fpath = str(file_or_path)
    else:
        fpath = file_or_path
    
    with open(fpath) as file:
        config = yaml.safe_load(file)

    return config