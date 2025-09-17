from datetime import datetime

from utils.utils import print_apartment_details

from learning_oops.exercises_applications.flatmates_bill.src.apartment import \
    Apartment
from learning_oops.exercises_applications.flatmates_bill.src.flat_mates import \
    FlatMate
from learning_oops.exercises_applications.flatmates_bill.src.rooms import Room

apartments: list[Apartment] = list()


def _configure_apartment():
    num_apartments = int(input("how many apartments you want to configure?"))
    for apartment in range(num_apartments):
        apartment_id = int(input("enter apartment id: "))
        assert type(apartment_id) == int, "apartment id must be an integer"
        apartment_name = input("enter apartment name: ")
        address = input("enter apartment address: ")
        num_rooms = int(input("enter number of rooms: "))
        rooms: list[Room] = list()
        room_counter = 1
        while room_counter <= num_rooms:
            room_num = int(input(f"enter room number for room number {room_counter}: "))
            if room_num in list(map(lambda x: x.room_id, rooms)):
                print(f"room number {room_num} already exists")
                continue
            attached_br_input = int(
                input("enter if attached bathroom. 1 for yes or 0 for no: ")
            )
            if attached_br_input == 0:
                attached_bathroom = True
            else:
                attached_bathroom = False
            rooms.append(Room(room_id=room_num, attached_bathroom=attached_bathroom))
            room_counter += 1

        apartments.append(
            Apartment(
                id=apartment_id,
                name=apartment_name,
                address=address,
                num_rooms=num_rooms,
                rooms_details=rooms,
            )
        )


def __person_details():
    name = input("enter person name: ")
    dob = input("enter person dob: ")
    origin = input("enter person origin: ")

    return FlatMate(name=name, dob=datetime.strptime(dob, "%Y-%m-%d"), origin=origin)


def _configure_flat_mate():
    while True:
        print("Lets get started with flat mates")
        print(
            "***********************Below are the apartments configurations********************"
        )
        print_apartment_details(apartments=apartments)
        apt_id = int(input("Which apartment would you like to configure?"))
        room_id = int(input("enter room id: "))

        apartment_ref = list(filter(lambda x: x.id == apt_id, Apartment.apartments))[0]
        room_ref = list(
            filter(lambda x: x.room_id == room_id, apartment_ref.room_details)
        )[0]
        apartment_ref.add_new_tenant(person=__person_details(), room=room_ref)

        print_apartment_details(apartments=apartments)
        if_exit = input("press 1 to exit")
        if if_exit == "1":
            break


def main():
    _configure_apartment()
    _configure_flat_mate()


if __name__ == "__main__":
    print("Welcome to FlatMates!")
    print("lets configure the apartments")

    main()
