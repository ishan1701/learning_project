import pytest

from learning_pytest.src.my_functions import add, divide


def test_add():
    result = add(1, 2)
    print(result)
    assert result == 3.0

    result = add("a", "b")
    assert result == "ab"


def test_divide():
    result = divide(1, 2)
    assert result == 0.5

    result = divide(10, 3)
    print(result)
    assert result == 3.33

    with pytest.raises(ValueError):
        result = divide("a", "b")
        print(result)


def test_divide_by_zero():
    with pytest.raises(ValueError):
        result = divide(10, 0)
