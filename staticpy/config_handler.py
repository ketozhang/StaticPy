import yaml
from pathlib import Path
PROJECT_PATH = Path.cwd()

CONFIGS_PATH = PROJECT_PATH / 'configs'
base_config = CONFIGS_PATH / 'base.yaml'
assert base_config.exists(), "`base.yaml` is required. Make one even if it's empty."

def get_config(name_or_path=base_config):
    if isinstance(name_or_path, Path):
        assert name_or_path.is_absolute(), "If pathlib.Path specified, it must be an absolute path."
        fpath = str(name_or_path)
    elif isinstance(name_or_path, str):
        fpath = CONFIGS_PATH / (name_or_path + '.yaml')
    else:
        raise ValueError("Argument (0) should either be a configuration name or path.")

    with open(fpath) as file:
        config = yaml.safe_load(file)

    return config