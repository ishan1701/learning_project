from learning_oops.exercises_applications.flatmates_bill.src.apartment import Apartment
from learning_oops.exercises_applications.flatmates_bill.src.rooms import Room
from utils.utils import read_json


def _load_apartment(file: str, data_directory: str):
    print("Loading apartment")
    data = read_json(file_name=file, data_dir=data_directory)
    for apt in data:
        apartment_rooms: list[Room] = list()
        for room in apt['rooms_details']:
            apartment_rooms.append(
                Room.from_json(room_id=room['room_id'], attached_bathroom=room['attached_bathroom'])
            )

        Apartment.from_json(id=apt['apartment_id'], name=apt['name'], address=apt['address'], num_rooms=apt['num_of_rooms'], rooms_details=apartment_rooms)

    print("Finished loading apartment")

def _load_flat_mates(file: str, data_directory):
    pass


def _load_bill(file: str):
    pass

def _load_vacation(file: str):
    pass

def main():
    _load_apartment(file='apartment.jsonl', data_directory='data')
    print(Apartment.apartments)


if __name__ == '__main__':
    main()
