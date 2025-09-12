from dataclasses import dataclass
from math import pi

from point import Point
from shapes import Shape


class Circle(Shape):
    def __init__(self, first_point: Point, second_point: Point):
        self._first_point = first_point
        self._second_point = second_point
        super().__init__(shape_type="circle")

    @property
    def first_point(self) -> Point:
        return self._first_point

    @property
    def second_point(self) -> Point:
        return self._second_point

    @property
    def radius(self) -> float:
        return Point.distance(self._first_point, self._second_point)

    @property
    def area(self) -> float:
        return pi * (self.radius**2)

    @property
    def perimeter(self) -> float:
        return 2 * pi * (self.radius**2)

    def if_point_lies(self, point: Point):
        point_distance_frm_center = Point.distance(self.first_point, point)

        if point_distance_frm_center < self.radius:
            return True
        else:
            return False

    def create_shape(self):
        print(f"creating shape for circle: {self}")

    def __repr__(self):
        return f"Circle created with radius {self.radius} with area {self.area})"
