import pytest
from fruit import Fruit, FruitBasket


@pytest.fixture
def fruit():
    return Fruit(
        name="apple",
        color="blue",
        growing_season="all year",
        classification="Fruit",
        price=22,
    )


def test_increase_price(fruit):
    increased_value = 10
    initial_price = fruit.price
    fruit.increase_price(increased_value)
    print(f"increased_value: {fruit.price}")

    assert fruit.price == (initial_price * increased_value / 100) + initial_price
