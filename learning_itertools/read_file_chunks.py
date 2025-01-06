from pathlib import Path


def _read_file(filename, parent, chunk_size: int):
    with open(Path(__file__).parent.joinpath(parent, filename)) as file:
        count=1
        prev=None
        for line in file:
            if count % chunk_size == 0:
                yield from [[prev.strip(), line.strip()]]
            prev = line
            count += 1
        if count % chunk_size == 0:
            yield from [[line.strip()]]



if __name__ == '__main__':
    filename = 'word_count.txt'
    parent_dir = 'data'
    chunks = 2

    contents = _read_file(filename, parent_dir, chunks)
    # print(next(contents))
    # print(next(contents))
    # print(next(contents))
    # print(next(contents))


    for chunk in contents:
        print(chunk)



