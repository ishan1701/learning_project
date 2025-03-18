from collections.abc import Iterable
from fruit import Fruit, FruitBasket


def _count_fruits_inner(fruits_basket: list[str]) -> dict[str, int]:
    fruit_count = dict()
    for fruit in fruits_basket:
        if fruit not in fruit_count:
            fruit_count[fruit] = 1
        else:
            fruit_count[fruit] += 1

    return fruit_count


def count_fruits(fruits_basket: Iterable[str]) -> dict[str, int]:
    print('__________________')
    if isinstance(fruits_basket, list):
        return _count_fruits_inner(fruits_basket)


    elif isinstance(fruits_basket, set):
        return _count_fruits_inner(list(fruits_basket))

    elif isinstance(fruits_basket, dict):
        fruit = list()
        for _, value in fruits_basket.items():
            fruit.append(value)
        return _count_fruits_inner(fruit)

    elif isinstance(fruits_basket, FruitBasket):
        fruit = list()
        for item in fruits_basket:
            fruit.append(item.name)
        return _count_fruits_inner(fruit)

    else:
        raise TypeError('Type is not implemented')


def main():
    fruits_basket_1: list[str] = ['apple', 'banana', 'banana', 'banana', 'banana']
    fruits_basket_2: dict[int, str] = {1: 'apple', 2: 'banana', 3: 'banana', 4: 'banana', 5: 'banana'}
    for basket in [fruits_basket_1, fruits_basket_2]:
        print(count_fruits(basket))

    f_1 = Fruit(name='apple', color='red', growing_season='winter', classification='fruit', price=100)
    f_2 = Fruit(name='apple', color='red', growing_season='winter', classification='fruit', price=100)
    print(count_fruits(FruitBasket([(f_1, 12), (f_2, 1)])))


if __name__ == '__main__':
    main()
