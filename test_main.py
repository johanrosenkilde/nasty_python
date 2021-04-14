from main import *

def test_multiply_by_3():
    assert multiply_by_3(3) == 9
    assert multiply_by_3(5) == 15

def test_multiply_by_3_again():
    assert multiply_by_3(-1) == -3