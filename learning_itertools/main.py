from pathlib import Path


def _get_iterator():
    list_1 = list(range(1, 10))
    print(list_1)
    iterator = iter(list_1)
    while True:
        try:
            print(next(iterator), end=' ')
        except StopIteration:
            break


def _read_file(file_name):
    file_path = Path(__file__).parent.joinpath('data', file_name)
    with open(file_path, "r") as f:
        for line in f:
            print(f'the typeis {type(line)}')
            yield line.strip()


def read_file(file_name)-> None:
    generator = _read_file(file_name)
    while True:
        try:
            print(next(generator))
        except StopIteration:
            break


if __name__ == '__main__':
    # _get_iterator()
    read_file(file_name='sample.txt')
