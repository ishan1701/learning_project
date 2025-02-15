from dataclasses import dataclass
from math import sqrt


@dataclass(frozen=True)
class Point:
    x: float
    y: float

    @staticmethod
    def distance(point_1: 'Point', point_2: 'Point'):
        return sqrt((point_1.x - point_2.x) ** 2 + (point_1.y - point_2.y) ** 2)

#The class name Point is enclosed in quotes ('Point') because the Point class is not fully defined at the time the type hint is written. This is called a forward reference.


