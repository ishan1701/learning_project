from datetime import date
from dataclasses import dataclass
from abc import ABC, abstractmethod


# @dataclass(frozen=True)
class Bill(ABC):
    def __init__(self, date: date, bill_number,amount, apt, room_number:int):
        self.date= date
        self.bill_number = bill_number
        self.amount = amount
        self.apt = apt
        self.room_number = room_number

    @classmethod
    @abstractmethod
    def from_json(cls, **kwargs):
        # return cls(json_data["date"], json_data["bill_number"], json_data["amount"], json_data["apt"],
        #            json_data["room_number"], True if json_data["is_fixed"]=="true" else False)
        pass


class Rental(Bill):
    def __init__(self, date: date, bill_number,amount, apt, room_number:int):
        self.is_fixed = True
        self.type = "Rental"
        super().__init__(date=date, bill_number=bill_number, amount=amount, apt=apt, room_number=room_number)

    @classmethod
    def from_json(cls, **kwargs):
        pass

class Electricity(Bill):
    def __init__(self, date: date, bill_number,amount, apt, room_number:int):
        self.is_fixed = False
        self.type = "Electricity"
        super().__init__(date=date, bill_number=bill_number, amount=amount, apt=apt, room_number=room_number)

    @classmethod
    def from_json(cls, **kwargs):
        pass

class Water(Bill):
    def __init__(self, date: date, bill_number,amount, apt, room_number:int):
        self.is_fixed = False
        self.type = "water"
        super().__init__(date=date, bill_number=bill_number, amount=amount, apt=apt, room_number=room_number)

    @classmethod
    def from_json(cls, **kwargs):
        pass


class Cleaning(Bill):
    def __init__(self, date: date, bill_number,amount, apt, room_number:int):
        self.is_fixed = True
        self.type = "Cleaning"
        super().__init__(date=date, bill_number=bill_number, amount=amount, apt=apt, room_number=room_number)

    @classmethod
    def from_json(cls, **kwargs):
        pass


def bill(type:str, **kwargs):

    #replacesd the below if else ladder to below
    # if type.lower() == "rent":
    #     return Rental.from_json(**kwargs)
    # elif type.lower() == "electricity":
    #     return Electricity.from_json(**kwargs)
    # elif type.lower() == "water":
    #     return Water.from_json(**kwargs)
    # elif type.lower() == "cleaning":
    #     return Cleaning.from_json(**kwargs)
    # else:
    #     raise ValueError("Type must be 'rent', 'electricity', 'water' or 'cleaning'")

    type = type.lower()
    bill_classes = {
        "rent": Rental,
        "electricity": Electricity,
        "water": Water,
        "cleaning": Cleaning
    }
    if type in bill_classes:
        return bill_classes[type].from_json(**kwargs)
    else:
        raise ValueError("Type must be 'rent', 'electricity', 'water', or 'cleaning'")


