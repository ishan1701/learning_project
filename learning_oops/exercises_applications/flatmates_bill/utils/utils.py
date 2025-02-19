import json

from learning_oops.exercises_applications.flatmates_bill.src.apartment import Apartment


def print_apartment_details(apartments: list[Apartment]) -> None:
    for apartment in apartments:
        print('\n')
        print('\n')
        print('\n')
        print('\n')
        print(f'***********************    NAME = {apartment.name}         ********************')
        print('\n')
        print('\n')
        print(f'***********************    AAP_ID = {apartment.id}          ********************')
        print('\n')
        print('\n')
        print(f'***********************    ROOM_CF = {apartment.room_config} ********************')
        print('\n')
        print('\n')
        print('\n')
        print('\n')

from typing import Generator, Dict
from pathlib import Path

def read_json(file_name: str, data_dir:str)->Generator[Dict, None, None]:

    with open(Path(__file__).parent.joinpath(data_dir, file_name)) as json_file:
        for line in json_file:
            yield json.loads(line)


def empty_apartment():
    pass

