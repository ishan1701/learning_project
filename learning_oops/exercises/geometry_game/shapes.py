from abc import ABC, abstractmethod
from point import Point
from math import sqrt


class Shape(ABC):
    def __init__(self, shape_type):
        self.shape = shape_type

    @property
    def shape_type(self):
        return f'the shape type is {self.shape} and shape class is {self.__class__.__name__}'

    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass

    # @classmethod
    # @abstractmethod
    # def from_class(cls, **kwargs):
    #     pass

    @abstractmethod
    def if_point_lies(self, point: Point):
        pass


    @abstractmethod
    def create_shape(self):
        pass


    # @staticmethod
    # @abstractmethod
    # def draw():
    #     pass


