from abc import ABC, abstractmethod


# Step 1: Create the DiscountStrategy interface
class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, total: float) -> float:
        pass


# Step 2: Implement the discount strategies
# TODO: Implement NoDiscount, PercentageDiscount, and FixedAmountDiscount classes


class NoDiscount(DiscountStrategy):
    def apply_discount(self, total: float) -> float:
        print("No discount applied")
        return total


class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage: float):
        self.percentage = percentage

    def apply_discount(self, total: float) -> float:
        print("Percentage discount applied")
        return total - (total * self.percentage / 100)


class FixedAmountDiscount(DiscountStrategy):
    def __init__(self, amount: float):
        self.amount = amount

    def apply_discount(self, total: float) -> float:
        print("Fixed amount discount applied")
        return total - self.amount


# Step 3: Implement the ShoppingCart class.. This is the context
class ShoppingCart:
    def __init__(self, discount_strategy: DiscountStrategy):
        self._discount_strategy = discount_strategy
        self.items: dict[str:float] = dict()

    @property
    def discount_strategy(self):
        return self._discount_strategy

    @discount_strategy.setter
    def discount_strategy(self, discount_strategy):
        self._discount_strategy = discount_strategy

    def add_item(self, item: str, price: float):
        if item in self.items:
            print("Item already added")
            return
        else:
            self.items[item] = price

    # TODO: Add the item with its price to the items dictionary

    def remove_item(self, item: str):
        if item not in self.items:
            print("Item not found")
            return
        else:
            del self.items[item]

    # TODO: Remove the item from the items dictionary if it exists

    def get_total(self) -> float:
        total: float = 0
        for item, value in self.items.items():
            total += value

        return total

    def get_total_after_discount(self) -> float:
        return self.discount_strategy.apply_discount(self.get_total())


# TODO: Calculate and return the total price of the items in the cart after applying the discount


# Step 4: Test your implementation
if __name__ == "__main__":
    # TODO: Create a shopping cart with a discount strategy
    cart = ShoppingCart(PercentageDiscount(10))

    # TODO: Add a few items
    cart.add_item("Item 1", 10.0)
    cart.add_item("Item 2", 20.0)
    cart.add_item("Item 3", 30.0)

    # TODO: Calculate and print the total price before discount
    print("Total before discount:", cart.get_total())

    # TODO: Calculate and print the total price after applying the discount
    print("Total after discount:", cart.get_total_after_discount())
