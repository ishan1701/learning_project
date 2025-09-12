from pathlib import Path

import yaml


def read_frm_yaml(file_path: Path) -> dict:
    with open(file_path, "r") as f:
        return yaml.safe_load(f)
