from collections import Counter


def count_fruits(basket: list[str]) -> dict[int, int]:
    counter = Counter(basket)
    print(counter.most_common())
    print(counter.most_common(3))

    iter = counter.elements()
    for element in iter:
        print(element)
    print("the values are")
    for k, v in counter.items():
        print(f"{k}: {v}")


if __name__ == "__main__":
    count_fruits([1, 2, 3, 1, 2, 3, 1, 2, 2, 2, 2])


## So the takeaway from this exercise is know about built-in libraries
## https://docs.python.org/3/py-modindex.html#cap-c
