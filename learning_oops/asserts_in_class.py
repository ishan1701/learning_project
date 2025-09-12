class Item:
    """
    Assertion is the statement to check the validations
    """

    def __init__(self, name: str, price: float, quantity: int = 0):
        assert (
            price > 0
        ), f"price should be greater than 0"  # this statement will check if the value is correct
        assert quantity > 0, f"quantity should be greater than 0"
        self.name = name
        self.price = price

    def __str__(self):
        return f"created {self.name} with price {self.price}"


if __name__ == "__main__":
    item_1 = Item(
        name="Item 1", price=10, quantity=10
    )  # this will lead an AssersionError exception
    # print(item_1)
    # print(item_1.price)
    print(Item.__dict__)  # All the attribute at tye class level

    print(item_1.__dict__)  # all the attributes at the instance level
