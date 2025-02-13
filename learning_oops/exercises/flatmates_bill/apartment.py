from flat_mates import FlatMate
from rooms import Room
from typing import Union
from bill import Rental, Cleaning


class Apartment:
    num_tenants: int = 0
    flat_mates: list[FlatMate] = []
    apartments: dict[int, 'Apartment'] = dict()

    def __init__(self, id: int, name: str, address: str, num_rooms: int, rooms_details: list[Room]):
        self._id = id
        self._name = name
        self._address = address
        self._num_rooms = num_rooms
        self.room_details: list[Room] = rooms_details
        if len(rooms_details) != self._num_rooms:
            raise ValueError("Number of rooms does not match number of rooms")

        if id in self.apartments:
            print(f'Apartment {id} already exists')
            print(f'skipping apartment {id}')

        else:
            self.apartments[id] = self

    @property
    def room_config(self):
        room_details = list()
        for room in self.room_details:
            room_details.append(
                {'room_id': room.room_id, 'have_bathroom': room.attached_bathroom, 'room_mates': room.rooms_mates})
        return room_details

    @property
    def num_rooms(self):
        return self._num_rooms

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def address(self):
        return self._address

    def add_new_tenant(self, person: FlatMate, room: Room):

        self.flat_mates.append(person)
        room.add_room_mate(person)
        self.num_tenants += 1

    def remove_tenant(self, person: FlatMate, room: Room):

        self.flat_mates.remove(person)
        room.remove_room_mate(person)
        self.num_tenants -= 1

    @classmethod
    def from_json(cls, **kwargs):
        return cls(id=kwargs['id'], name=kwargs['name'], address=kwargs['address'], num_rooms=kwargs['num_rooms'],
                   rooms_details=kwargs['rooms_details'])

    def __repr__(self):
        return f'Apartment(name={self.name}, address={self.address}, num_rooms={self.num_rooms},room_details={self.room_details})'

    @classmethod
    def get_apartment_bills(cls):
        pass

    def split_bill(self, bill: Union[Rental, Cleaning]):
        if not bill.is_fixed:
            raise ValueError(f'Bill {bill.__class__.__name__} should be fixed.'
                             f'Fixed bills needs to be calculated at the room level')

        if len(self.flat_mates) == 0:
            print(f"Apartment {self.id} is empty. Hence, not splitting bill.")
            return

        shared_amount = bill.amount / len(self.flat_mates)
        for flat_mate in self.flat_mates:
            flat_mate.bill_amount += shared_amount


    def print_bills(self):
        for apt in self.apartments.values():
            pass

