import csv
import json
import sys


## read the csv file as dict
def parse_file_dict_reader(file_path: str):
    with open(file_path, mode="r") as f_read:
        data = csv.DictReader(f_read)
        for row in data:
            print(row)
            for key, value in row.items():
                print(f"{key}: {value}")


def parse_file(file_path: str):
    with open(file_path, mode="r") as f_read:
        csv_reader = csv.reader(f_read)
        for row in csv_reader:
            print(row)
            # print(type(row))


def read_json(file_path: str):
    with open(file_path, mode="r") as f_read:
        data = json.load(f_read)
        for row in data:
            print(row)
            print(type(row))


def parse_xml(file_path: str):
    from xml.etree import ElementTree as ET

    with open(file_path, mode="r") as f_read:
        tree = ET.parse(f_read)
        root = tree.getroot()
        for element in root.iter():
            if len(element.items()) > 0:
                print(element.attrib)


if __name__ == "__main__":
    # parse_file_dict_reader(file_path='sample.csv')
    # parse_file(file_path='sample.csv')
    # read_json('sample.json')
    parse_xml("sample.xml")
