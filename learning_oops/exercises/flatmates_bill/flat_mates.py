from datetime import date


class FlatMate:
    number = 0

    def __init__(self, name: str, dob: date, origin: str):
        self._name = name
        self._dob = dob
        self.origin = origin
        self.number += 1

    @property
    def name(self):
        return self._name

    @property
    def dob(self):
        return self._dob

    @property
    def age(self):
        return date.today().year - self.dob.year

    def __repr__(self):
        return f'FlatMate({self.name}, {self.age}, {self.origin})'

    @classmethod
    def from_json(cls, **kwargs):
        return cls(kwargs['name'], kwargs['dob'], kwargs['origin'])
