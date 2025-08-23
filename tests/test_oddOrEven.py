import pytest
from oddOrEven import odd_or_even

def test_odd_or_even():
    assert odd_or_even(10) == "Even"
    assert odd_or_even(11) == "Odd"
    assert odd_or_even(15) == "Odd"
    assert odd_or_even(1.5) == "Provide an Integer"
