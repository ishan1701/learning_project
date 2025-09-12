from datetime import date
from typing import Union

from flat_mates import FlatMate
from rooms import Room

from learning_oops.exercises_applications.flatmates_bill.src.apartment import \
    Apartment


class Vacation:
    def __init__(
        self,
        start_date: date,
        end_date: date,
        flatmate_id: int,
        apt_id: int,
        apt_room_id: int,
    ):
        self.start_date = start_date
        self.end_date = end_date
        self.flatmate_id = flatmate_id
        self.apt_id = apt_id
        self.apt_room_id = apt_room_id

    @classmethod
    def from_date(cls, **kwargs):
        return cls(
            start_date=kwargs["start_date"],
            end_date=kwargs["end_date"],
            flatmate_id=kwargs["flatmate_id"],
            apt_room_id=kwargs["apt_room_id"],
        )

    @property
    def vacation_days(self):
        return (self.end_date - self.start_date).days

    def allocate_vacation_to_flatmates(self):
        room: Union[Room, None] = None
        flatmate: Union[FlatMate, None] = None

        apt = Apartment.apartments.get(self.apt_id, None)
        if apt is None:
            raise ValueError(f"Apartment with {self.apt_id} not found")

        for room_detail in apt.room_details:
            if room_detail.room_id == self.apt_room_id:
                room = room_detail
                break

        if room is None:
            raise ValueError(f"Apartment with {self.apt_id} not found")

        for flatmate in room.rooms_mates:
            if flatmate.id == self.flatmate_id:
                flatmate = flatmate
                break

        if flatmate is None:
            raise ValueError(f"Apartment with {self.apt_id} not found")

        flatmate.vacation_days = self.vacation_days
