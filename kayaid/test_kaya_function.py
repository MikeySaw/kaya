import pytest
from kaya_function import kaya_eq

def test_valid_input():
    # Test with valid input values
    result = kaya_eq(82.4, 44, 5, 0.05)
    assert result == 722.8

def test_negative_input():
    # Test with negative population size
    with pytest.raises(ValueError):
        kaya_eq(-82.4, 44, 5, 0.05)

    # Test with negative GDP per capita
    with pytest.raises(ValueError):
        kaya_eq(82.4, -44, 5, 0.05)

    # Test with negative energy intensity
    with pytest.raises(ValueError):
        kaya_eq(82.4, 44, -5, 0.05)

    # Test with negative carbon intensity
    with pytest.raises(ValueError):
        kaya_eq(82.4, 44, 5, -0.05)
