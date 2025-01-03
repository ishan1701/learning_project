from typing import Generator
from pathlib import Path


def count_words(text: str):
    words = text.split(' ')
    print(words)
    if len(words) == 1:
        yield words
    else:
        yield list()


def read_lines(file_name: str):
    with open(Path(__file__).parent.joinpath('data', file_name), 'r') as file:
        for line in file:  # looping is required
            if line.strip() != '':
                yield count_words(line.strip())
            else:
                print('line with emprt')


if __name__ == '__main__':
    word_count = read_lines(file_name='word_count.txt')
    num_words = 0
    print(word_count)

    for word in word_count:
        num_words += len(next(word))

    print(num_words)
