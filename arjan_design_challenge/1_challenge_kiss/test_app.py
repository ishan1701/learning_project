import pytest
from app import count_fruits


def test_count_fruits():
    # test with list
    fruits_basket = ["apple", "orange"]
    print(fruits_basket)
    fruits_count_actual = count_fruits(fruits_basket)
    fruits_count_expected = {"apple": 1, "orange": 1}

    assert fruits_count_expected == fruits_count_actual

    # case 2: passing unsupported types
    with pytest.raises(expected_exception=TypeError, match="Type is not implemented"):
        count_fruits("apple")
