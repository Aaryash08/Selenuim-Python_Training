import pytest
from Q2 import multiply, divide

def test_multiplication(numbers):
    a, b = numbers
    assert multiply(a, b) == 50

def test_division(numbers):
    a, b = numbers
    assert divide(a, b) == 2

def test_division_by_zero(numbers):
    a, _ = numbers
    with pytest.raises(ValueError):
        divide(a, 0)

def test_calculator_name(calculator_name):
    assert calculator_name == "Simple Calculator"
