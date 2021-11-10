from main import *

def test_multiply_by_3():
    assert multiply_by_3(3) == 9
    assert multiply_by_3(5) == 15

def test_multiply_by_3_again():
    assert multiply_by_3(-1) == -3

def test_arachid():
    assert arachid(3) == 6
    assert arachid(5) == 10

def test_function_you_can_never_guess():
    assert function_you_can_never_guess(1) == "a"
    assert function_you_can_never_guess("u") == "a"

def test_failing_my_own_test():
    assert failing_my_own_test(1) == 2
