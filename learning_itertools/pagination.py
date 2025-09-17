def _generate_pages(size, data):
    start = 0
    end = size

    while True:
        yield data[start:end]
        start = end
        end = start + size


if __name__ == "__main__":
    page_size = 3
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 12]

    generators = _generate_pages(page_size, data)

    for generator in generators:
        if len(generator) == 0:
            break
        print(generator)
