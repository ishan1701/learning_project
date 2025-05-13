import json
from pathlib import Path


def if_file_exists(path: Path) -> bool:
    return path.exists()


def if_empty_file(path: Path) -> bool:
    return path.stat().st_size == 0


def read_json_file(path: Path) -> dict | None:
    if not if_file_exists(path) or if_empty_file(path):
        print(f"{path} does not exist")
        return dict()

    with open(path) as json_file:
        data = json.load(json_file)

    return data


def write_json_file(path: Path, data: dict):
    with open(path, "w") as json_file:
        json.dump(data, json_file, indent=4)
