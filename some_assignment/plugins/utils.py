import yaml
from pathlib import Path


def load_yaml_file(file_path: Path) -> dict:
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)


def load_sql_file(file_name: Path) -> str:
    with open(file_name, 'r') as file:
        contents = file.read()
    return contents
