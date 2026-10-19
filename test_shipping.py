
import pytest
from shipping import shipping_fee


# Rule 1: Weight must be greater than zero.
@pytest.mark.parametrize("weight", [0, -1, -5])
def test_invalid_weight(weight):
    with pytest.raises(ValueError):
        shipping_fee(weight)


# Rule 2: Weight up to 1 kg costs 40 baht.
# BUG: Exactly 1 kg incorrectly costs 60 baht.
@pytest.mark.parametrize("weight, expected", [
    (0.1, 40),
    (0.5, 40),
    (1.0, 40),
])
def test_small_parcel(weight, expected):
    assert shipping_fee(weight) == expected


# Rule 3: More than 1 kg up to 5 kg costs 60 baht.
@pytest.mark.parametrize("weight, expected", [
    (1.1, 60),
    (3.0, 60),
    (5.0, 60),
])
def test_medium_parcel(weight, expected):
    assert shipping_fee(weight) == expected


# Rule 4: Each started kilogram above 5 costs 10 baht.
# BUG: int() rounds down instead of rounding up.
@pytest.mark.parametrize("weight, expected", [
    (5.2, 70),
    (6.0, 70),
    (6.1, 80),
    (7.5, 90),
])
def test_heavy_parcel(weight, expected):
    assert shipping_fee(weight) == expected
