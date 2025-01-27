from typing import List
from functools import reduce


class Item:
    all = []

    def __init__(self, name: str, price: float):
        assert price > 0.0, f'price must be positive'
        self._name = name
        self._price = price
        Item.all.append(self)

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    def __repr__(self):
        return f'{self.__class__.__name__}({self._name}, {self._price})'


class ItemShipment:
    def __init__(self, items: List[Item]):
        self._items = items

    def shipment_costs(self):
        return reduce(lambda x, y: x + y, map(lambda x: x.price, self._items))


class Phone(Item):

    def __init__(self, name: str, price: float, broken_phones=0):
        self._broken_phones = broken_phones
        super().__init__(name=name, price=price)


class Laptop(Item):

    def __init__(self, name: str, price: float, os_type=0):
        self._os = os_type
        super().__init__(name=name, price=price)


if __name__ == '__main__':
    p1 = Phone(name='p1', price=100, broken_phones=1)
    p2 = Phone('P2', 3.0)
    l1 = Laptop(name='l1', price = 112)
    for item in [p1, p2,l1]:
        print(item)

    it_shp = ItemShipment([p1, p2, l1])

    print(it_shp.shipment_costs())
