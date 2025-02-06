from flat_mates import FlatMate
from rooms import Room


class Apartment:
    num_tenants = 0
    flat_mates = []

    def __init__(self, name: str, address: str, num_rooms: int, rooms_details:list[Room]):
        self._name = name
        self._address = address
        self._num_rooms = num_rooms
        self.room_details: list[Room] = rooms_details
        if len(rooms_details) != self._num_rooms:
            raise ValueError("Number of rooms does not match number of rooms")

    @property
    def rooms(self):
        return self._num_rooms

    @property
    def name(self):
        return self._name

    @property
    def address(self):
        return self._address

    def add_new_tenant(self, person: FlatMate, room: Room):
        self.num_tenants += 1
        self.flat_mates.append(person)
        room.add_room_mate(person)

    def remove_tenant(self, person: FlatMate, room: Room):
        self.num_tenants -= 1
        self.flat_mates.remove(person)
        room.remove_room_mate(person)

    def __repr__(self):
        return f'Apartment(name={self.name}, address={self.address})'