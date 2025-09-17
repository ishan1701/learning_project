import argparse
import math


def _operations(number: int):
    print(f"The number you provided is {number}")
    if number > 100:
        raise ValueError("greater than hundred")

    elif number < 0:
        raise ValueError("less than zero")

    else:
        return math.sqrt(number)


def _check_count(count):
    print(type(count))
    if type(count == list):
        print(sum(count))
    else:
        print(type(count))


def _check_numbers(numbers):
    print(type(numbers))


def _parse_args():
    parser = argparse.ArgumentParser(description="check the params")
    parser.add_argument("--count", type=int, nargs="+", help="provide a number")
    parser.add_argument("some_number", type=int, help="provide a number")
    parser.add_argument(
        "--numbers", type=int, nargs="+", help="provide a list of numbers"
    )
    arguments = parser.parse_args()
    return arguments


if __name__ == "__main__":
    args = _parse_args()
    print(args)
    print(f"The operation value is {_operations(args.some_number)}")
    _check_count(args.count)
