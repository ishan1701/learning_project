from flat_mates import FlatMate
from bill import Bill
from functools import reduce


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

    def split_bill(self, bill: Bill):
        if self.if_room_empty:
            print(f"Room {self.room_id} is empty. Hence, not splitting bill.")
            return
        if bill.is_fixed:
            for room_mate in self.rooms_mates:
                room_mate.bill_amount += (bill.amount / len(self.rooms_mates))
        else:
            total_roommate_days = int(
                reduce(lambda x, y: (30 - x.vacation_days) + (30 - y.vacation_days), self.rooms_mates))

            cost_per_day = bill.amount / total_roommate_days
            for room_mate in self.rooms_mates:
                room_mate.bill_amount += (room_mate.vacation_days * cost_per_day)

    def __repr__(self):
        return f"Room(room_id = {self.room_id}, attached_bathroom = {self.attached_bathroom})"
