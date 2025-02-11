from datetime import date
from dataclasses import dataclass


@dataclass(frozen=True)
class Bill:
    date: date
    bill_number: int
    amount: float
    apt: int
    room_number: int
    is_fixed: bool

    @classmethod
    def from_json(cls, json_data):
        return cls(json_data["date"], json_data["bill_number"], json_data["amount"], json_data["apt"],
                   json_data["room_number"], True if json_data["is_fixed"]=="true" else False)
