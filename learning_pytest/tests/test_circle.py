import math

import pytest

from learning_pytest.src.class_based_tests import Circle


@pytest.fixture
def circle():
    return Circle(radius=40)


def test_area(circle):
    result = circle.area()
    print(result)
    assert result == round((math.pi * 40 * 40), 2)
