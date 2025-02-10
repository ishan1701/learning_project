from flat_mates import FlatMate
from learning_oops import self


class Room:
    num = 0
    rooms_mates: list[FlatMate] = []
    MAX_ROOM_MATE = 2

    def __init__(self, room_id: int, attached_bathroom: bool):
        self.room_id = room_id
        self.attached_bathroom = attached_bathroom

    def add_room_mate(self, mate: FlatMate):
        print(f"Adding room mate {mate}")
        if self.num == self.MAX_ROOM_MATE:
            raise ValueError(f"Room {self.num} exceeds maximum number of {self.MAX_ROOM_MATE}")
        self.rooms_mates.append(mate)
        self.num += 1

    def remove_room_mate(self, mate: FlatMate):
        if self.num == 0:
            raise ValueError(f"Room is empty")
        self.rooms_mates.remove(mate)
        self.num -= 1

    @property
    def if_room_empty(self):
        return True if self.num == 0 else False

    @property
    def rooms_status(self):
        return f'{self.room_id} has attached br sd {self.attached_bathroom} with flatmates- {self.rooms_mates}'

    @classmethod
    def from_json(cls, **kwargs):
        return cls(kwargs["room_id"], kwargs["attached_bathroom"])

    def __repr__(self):
        return f"Room(room_id = {self.room_id}, attached_bathroom = {self.attached_bathroom})"
