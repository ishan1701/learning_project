import os
from pathlib import Path

import yaml


def read_config_file(file_name: str):
    print(Path(__file__).parent.joinpath("some", file_name))
    with open(Path(__file__).parent.joinpath("some", file_name), "r") as file:
        data = yaml.safe_load(file)

        print(f" config is {data}")

    with open(os.path.join(os.path.dirname(__file__), "some", file_name)) as file:
        data = yaml.safe_load(file)
    print(data)


if __name__ == "__main__":
    read_config_file("config.yaml")
