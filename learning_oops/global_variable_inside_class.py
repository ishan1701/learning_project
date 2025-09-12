from typing import Generator, List


class Item:
    all: list = list()  # Here is created the class variable

    def __init__(self, name: str, price: float, quantity: int = 0):
        assert (
            price > 0
        ), f"price should be greater than 0"  # this statement will check if the value is correct
        assert quantity > 0, f"quantity should be greater than 0"
        self.name = name
        self.price = price

        Item.all.append(self)  # add the element to the class method
        # self.all.append(self) # this us also do the same but above one is more correct to specify

    def __repr__(self):
        return f"created {self.name} with price {self.price}"


def generator(instance_list: list[Item]) -> Generator[Item, None, None]:
    for item in instance_list:
        yield item.name, item.price
        print(f"After yielding. {item}")


if __name__ == "__main__":
    item_1 = Item(name="mobile", price=10, quantity=10)
    item_2 = Item(name="lap1", price=20, quantity=10)
    item_3 = Item(name="lap2", price=20, quantity=10)
    item_5 = Item(name="lap3", price=20, quantity=10)

    for item in [item_1, item_2, item_3, item_5]:
        print(item)

    # via normal

    for instance in Item.all:
        print(instance)
        print(instance.name)

    # via generators
    itr = generator(Item.all)

    for name, price in itr:
        print(name, price)
        print(type(itr))
