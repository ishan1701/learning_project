from datetime import date

from learning_oops.exercises_applications.flatmates_bill.src.bill import Bill


class FlatMate:
    number = 0

    def __init__(self, id: int, name: str, dob: date, origin: str, vacation_days: int = 0):
        self._id = id
        self._name = name
        self._dob = dob
        self.origin = origin
        self.number += 1
        self.__vacation_days = vacation_days
        self.__bill_amount = 0

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def dob(self):
        return self._dob

    @property
    def age(self):
        return date.today().year - self.dob.year

    @property
    def vacation_days(self):
        return self.__vacation_days

    @vacation_days.setter
    def vacation_days(self, vacation_days: int):
        self.__vacation_days = vacation_days

    @property
    def bill_amount(self):
        return self.__bill_amount

    @bill_amount.setter
    def bill_amount(self, bill_amount: int):
        self.__bill_amount = bill_amount

    @classmethod
    def from_json(cls, **kwargs):
        return cls(kwargs['id'], kwargs['name'], kwargs['dob'], kwargs['origin'])

    def pay_bill(self, bill: Bill):
        pass
        # write logic to pay the bill and update the owner association

    def __repr__(self):
        return f'FlatMate({self.name}, {self.age}, {self.origin})'


