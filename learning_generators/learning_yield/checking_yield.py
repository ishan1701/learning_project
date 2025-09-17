def process(item):
    with open("sample.txt", "w") as file:
        file.write(str(item))
        file.write("\n")


def data_generator(big_list):
    print(big_list)
    for item in big_list:
        result = process(item)
        print(result)
        yield result


if __name__ == "__main__":
    lst = []
    for i in range(1, 100):
        lst.append(i)
    data_generator(lst)
