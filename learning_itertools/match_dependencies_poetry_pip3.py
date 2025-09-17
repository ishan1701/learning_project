from pathlib import Path


def _if_present_toml(package, toml_file_name):
    with open(Path(__file__).parent.parent.joinpath(toml_file_name), "r") as toml_file:
        for toml_line in toml_file:
            toml_package = toml_line.strip().split("=")[0].strip()
            # print(f'toml_package is {toml_package}')
            # print(f'package is {package}')
            if package == toml_package:
                return True
        return False


def read_file(file_name, toml_file_name):
    with open(Path(__file__).parent.parent.joinpath(file_name)) as f:
        for line in f:
            if not _if_present_toml(
                package=line.strip().split("==")[0], toml_file_name=toml_file_name
            ):
                yield f'{line.strip().split("==")[0]}="^{line.strip().split("==")[1]}"'


if __name__ == "__main__":
    generator = read_file("requirements.txt", toml_file_name="pyproject.toml")

    print(generator)
    for package in generator:
        print(package)
