from datetime import date
from dataclasses import dataclass

@dataclass(frozen=True)
class Bill:
    bill_number: str
    bill_date: date
    bill_amount: float
