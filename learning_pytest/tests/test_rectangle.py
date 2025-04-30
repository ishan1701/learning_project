import math

from learning_pytest.src.class_based_tests import Rectangle
import pytest


@pytest.fixture
def rectangle():
    return Rectangle(width=10, height=10)


def test_area(rectangle):
    result = rectangle.area()

    assert result == round((10 * 10), 2)


@pytest.mark.parametrize('width, height, expected_area', [(2, 2, 4), (5, 6, 30)])
def test_rectangle_area(width, height, expected_area):
    assert Rectangle(width=width, height=height).area() == expected_area


@pytest.mark.skip
def test_rectangle_center(rectangle):
    pass