from shapes import Shape
from point import Point
from typing import Dict


class Rectangle(Shape):
    def __init__(self, first_point: Point, second_point: Point):
        self._first_point = first_point
        self._second_point = second_point
        super().__init__(shape_type='rectangle')

    @property
    def length(self) -> float:
        return abs(self._second_point.y - self._first_point.y)

    @property
    def breadth(self) -> float:
        return abs(self._second_point.x - self._first_point.x)

    @property
    def first_point(self) -> Point:
        return self._first_point

    @property
    def second_point(self) -> Point:
        return self._second_point

    @property
    def area(self):
        return self.length * self.breadth

    @property
    def perimeter(self):
        return 2 * self.length + self.breadth


    def if_point_lies(self, point: Point):
        if self.first_point.x < point.x < self.second_point.x and self.first_point.y < point.y < self.second_point.y:
            return True
        else:
            return False

    def create_shape(self):
        print(f' the self is {self}')
        print(f'creating shape for {self.shape}')

    def __repr__(self):
        return f'rectangle  created with length {self.length} breadth {self.breadth} and area {self.area})'



