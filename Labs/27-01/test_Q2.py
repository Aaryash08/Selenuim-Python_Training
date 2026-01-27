import unittest
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y
class TestCalculator(unittest.TestCase):

    def test_add(self):
        result = add(10, 5)
        self.assertEqual(result, 15)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        result = subtract(10, 5)
        self.assertEqual(result, 5)
        self.assertEqual(subtract(-1, 1), -2)

    def test_multiply(self):
        result = multiply(3, 7)
        self.assertEqual(result, 21)
        self.assertEqual(multiply(-1, 5), -5)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        result = divide(10, 2)
        self.assertEqual(result, 5)
        self.assertEqual(divide(5, 2), 2.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)

if __name__ == '__main__':
    unittest.main()