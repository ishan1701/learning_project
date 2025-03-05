from pathlib import Path
import csv
from typing import Generator


class Item:
    '''
    Scenario: I have a class which represents an Item.
    Now the requirement is to read the file and create the object by reading line by line.
    Here the class method can be used.
    '''

    def __init__(self, name: str, price: float, quantity: int = 0):
        assert price > 0, f'price should be greater than 0'  # this statement will check if the value is correct
        assert quantity > 0, f'quantity should be greater than 0'
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        return f'Item({self.name}, {self.price})'

    @classmethod
    def read_csv(cls, file_path: str, file_name: str)->Generator[iter, None, None]:
        with open(Path(__file__).parent.joinpath(file_path, file_name), 'r') as f_open:
            reader = csv.reader(f_open, delimiter=',', skipinitialspace=True)

            next(reader)  ## to skip the header

            for row in reader:
                yield cls(name=row[0], price=float(row[1]), quantity=int(row[2]))


if __name__ == '__main__':
    items = Item.read_csv(file_path='data', file_name='items.csv')
    print(items)

    for item in items:
        print(item)
        print(item.name, item.price)