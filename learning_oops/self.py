class Point:
    def __init__(ths, x, y):  # Here self can be replaced with any name
        ths.x = x
        ths.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


def main():
    point = Point(x=1, y=2)

    print(point)


if __name__ == "__main__":
    main()
