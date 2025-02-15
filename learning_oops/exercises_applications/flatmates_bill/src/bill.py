from datetime import date
from dataclasses import dataclass
from abc import ABC, abstractmethod


# @dataclass(frozen=True)
class Bill(ABC):
    '''
    Purpose : This class is an abstract class for the bill which can be generated for an apartment.
            This file contains a factory method to return the instance of class for each bill.
    '''
    def __init__(self, date: date, bill_number,amount, apt, room_number:int):

        self.date= date
        self.bill_number = bill_number
        self.amount = amount
        self.apt = apt
        self.room_number = room_number

    @classmethod
    @abstractmethod
    def from_json(cls, **kwargs):
        '''
        Purpose: Method to create a Bill object from json. A file contains all the bills which can be generated for an apartment.
        :param kwargs: keyword args

        '''
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


