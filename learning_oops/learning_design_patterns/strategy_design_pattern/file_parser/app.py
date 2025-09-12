#
# step 1: Create an interface with abstract method called parse
# step 2: create concreate classes like csv, xml and json
# step 3: implement the parse method
#
# step 4: Create context, taking interface name
# step 5: Add a method to context to run the parser
#
import csv
import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
from typing import Any, Dict, List


class FileParser(ABC):
    @abstractmethod
    def parse_file(self, file_path: str) -> list[dict]:
        pass


class CSVParser(FileParser):
    def parse_file(self, file_path: str) -> list[dict]:
        data: list[dict[str, str]] = list()
        with open(file_path, mode="r") as f_read:
            lines = csv.DictReader(f_read)
            for row in lines:
                for key, value in row.items():
                    data.append({key: value})
        return data


class JSONParser(FileParser):
    def parse_file(self, file_path: str) -> list[dict]:
        data: list[dict[str, str]] = list()
        with open(file_path, mode="r") as f_read:
            lines = json.load(f_read)
            for row in lines:
                data.append(row)
        return data


class XMLParser(FileParser):
    def parse_file(self, file_path: str) -> list[dict]:
        data: list[dict[str, str]] = list()
        with open(file_path, mode="r") as f_read:
            tree = ET.parse(f_read)
            root = tree.getroot()

            for element in root.iter():
                if len(element.items()) > 0:
                    data.append({element.tag: element.text})

        return data


# context class
class FileReader:
    def __init__(self, file_parser: FileParser):
        self._parser = file_parser

    @property
    def parser(self) -> FileParser:
        return self._parser

    @parser.setter
    def parser(self, parser: FileParser):
        self._parser = parser

    def read_file(self, file_path: str) -> List[Dict[str, Any]]:
        return self.parser.parse_file(file_path)


# Step 4: Test your implementation
if __name__ == "__main__":
    # TODO: Create a file reader with a CSVParser
    reader = FileReader(XMLParser())

    # TODO: Read a sample CSV file and print the list of dictionaries
    data = reader.read_file("sample.xml")
    print(data)

    reader = FileReader(JSONParser())
    data = reader.read_file("sample.json")
    print(data)

    reader = XMLParser()
    data = reader.parse_file("sample.xml")
    print(data)
