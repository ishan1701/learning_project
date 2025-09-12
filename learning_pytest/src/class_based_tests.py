import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round((math.pi * self.radius * self.radius), 2)

    def perimeter(self):
        return round((2 * math.pi * self.radius * self.radius), 2)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return round((self.width * self.height), 2)

    def perimeter(self):
        return round(2 * (self.width + self.height), 2)


if __name__ == "__main__":
    c = Circle(5)
    print(c.area())
    print(c.perimeter())
