from abc import ABC, abstractmethod


class Item(ABC):
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def increase_price(self, increase_value: float):
        self.price = self.price + (self.price * increase_value / 100)

    def decrease_price(self, decrease_value: float):
        self.price = self.price - (self.price * decrease_value / 100)


class Fruit(Item):
    def __init__(self, name: str, color: str, growing_season: str, classification: str, price: float):
        super().__init__(name, price)
        self.color = color
        self.growing_season = growing_season
        self.classification = classification


class FruitBasket:
    def __init__(self, items: list[(Item, float)]):
        self.items = items
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.items):
            item = self.items[self.index][0]
            self.index += 1
            return item

        else:
            raise StopIteration


# def main():
#     f_1 = Fruit(name='w_apple', color='red', growing_season='winter', classification='fruit', price=100)
#     f_2 = Fruit(name='r_apple', color='red', growing_season='winter', classification='fruit', price=100)
#     # color: str, growing_season: str, classification: str, price: float
#     f_b = FruitBasket([(f_1,12), (f_2,1)])
#
#     for fruit in f_b:
#         print(fruit.name, fruit.price)
#
#
# if __name__ == '__main__':
#     main()
