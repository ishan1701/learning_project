from typing import Union


def add(n1: Union[int, float, str], n2: Union[int, float, str]):
    if isinstance(n1, str) or isinstance(n1, str):
        return f"{n1}{n2}"
    else:
        return float(n1 + n2)


def divide(n1: Union[int, float], n2: Union[int, float]):
    if n2 == 0:
        raise ValueError("cannot divide by zero")
    return round(float(n1) / n2, 2)


if __name__ == "__main__":
    print(divide(1, 2))
    print(add("a", "b"))
