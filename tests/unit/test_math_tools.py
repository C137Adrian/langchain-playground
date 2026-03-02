from src.tools.math_tools import (
    add_numbers, subtract_numbers, multiply_numbers, divide_numbers
)

def test_add_numbers():
    assert add_numbers.invoke({"a": 2, "b": 3}) == 5

def test_subtract_numbers():
    assert subtract_numbers.invoke({"a": 5, "b": 2}) == 3

def test_multiply_numbers():
    assert multiply_numbers.invoke({"a": 4, "b": 3}) == 12

def test_divide_numbers():
    assert divide_numbers.invoke({"a": 10, "b": 2}) == 5
