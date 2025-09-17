from typing import Generator


def _filter_even_numbers(data) -> Generator[int, None, None]:
    counter = 0

    while counter < len(data):
        if data[counter] % 2 == 0:
            yield data[counter]
        counter += 1


if __name__ == "__main__":
    generator = _filter_even_numbers(data=range(1, 1000))

    for item in generator:
        print(item)
