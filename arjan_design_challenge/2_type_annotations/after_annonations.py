from typing import (Any, Callable, Generator, Iterable, Optional, Tuple,
                    TypeVar, Union)

T = TypeVar("T")
U = TypeVar("U")


def filter_odd_numbers(numbers: Iterable[int]) -> list[int]:
    """Filters odd numbers from a sequence of numbers."""
    result: list[int] = list()
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result


def square_numbers(
    numbers: Union[Iterable[int] | Iterable[float]],
) -> list[int | float]:
    """Square numbers in a sequence."""
    result: list[int | float] = list()
    for num in numbers:
        result.append(num**2)
    return result


def count_chars(words: Iterable[str]) -> list[int]:
    """Counts the number of characters in a sequence of words."""
    result: list[int] = list()
    for word in words:
        result.append(len(word))
    return result



def process_data(
    data,
    filter_func: Callable[[T], T] | None = None,
    process_func: Callable[[T | U], U] | None = None,
):  # process_func: Union[Callable[[T | U], U], None] = None): before 3.10 version
    """Applies filter_func and process_func on a data sequence."""
    if filter_func:
        data = filter_func(data)
    if process_func:
        return process_func(data)
    return data


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    result = process_data(numbers, filter_odd_numbers, square_numbers)
    print(result)

    words = ["apple", "banana", "cherry"]
    result2 = process_data(words, process_func=count_chars)
    print(result2)


if __name__ == "__main__":
    main()

# the main key takeaway of this exercise is to learn about the typing module
# after python 3.10 | can be used in place of Union. Its also true using list rather List from typing or dict rather using Dict from typing
# the return type should be very precise, but the args should be broad. What it means in the above examples, the return type MUST be precise to list[whatever] but the arg type SHOULD be Iterable
