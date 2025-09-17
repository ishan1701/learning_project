import csv
import json
from abc import ABC, abstractmethod
from pathlib import Path

import yaml


class FileLoader(ABC):
    def __init__(self, path, name):
        self.path = path
        self.name = name

    @classmethod
    @abstractmethod
    def read_from_path(cls, path, name):
        """
        Create the object after opening the file . The implementation is not completed here.
        """
        pass

    @property
    def absolute_path(self):
        return Path(self.path).joinpath(self.name)


class JsonLoader(FileLoader):
    def __init__(self, path, name):
        self.file_type = "json"
        super().__init__(path=path, name=name)

    @classmethod
    def read_from_path(cls, path, name):
        """
        Create the object after opening the file . The implementation is not completed here.
        """
        return cls(path=path, name=name)


class YamlLoader(FileLoader):
    def __init__(self, path, name):
        self.file_type = "yaml"
        super().__init__(path=path, name=name)

    @classmethod
    def read_from_path(cls, path, name):
        """
        Create the object after opening the file . The implementation is not completed here.
        """
        return cls(path=path, name=name)


class CSVLoader(FileLoader):
    def __init__(self, path, name):
        self.file_type = "csv"
        super().__init__(path=path, name=name)

    @classmethod
    def read_from_path(cls, path, name):
        """
        Create the object after opening the file . The implementation is not completed here.
        """
        return cls(path=path, name=name)


class ParquetLoader(FileLoader):
    def __init__(self, path, name):
        self.file_type = "parquet"
        super().__init__(path=path, name=name)

    @classmethod
    def read_from_path(cls, path, name):
        """
        Create the object after opening the file . The implementation is not completed here.
        """
        return cls(path=path, name=name)


if __name__ == "__main__":
    y1 = YamlLoader.read_from_path(path="test.yaml", name="test")

    j1 = JsonLoader.read_from_path(path="test.json", name="test")

    print(j1.absolute_path)
    print(j1.file_type)

    print(y1.absolute_path)
    print(y1.file_type)
