import pytest 
from mult3or5 import main

def test_multiple_of_3_or_5():
    assert main(10) == 23
    assert main(20) == 78
    assert main(1000) == 233168

