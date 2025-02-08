from apartment import Apartment


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