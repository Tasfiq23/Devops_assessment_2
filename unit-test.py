import unittest

from operations import add, subtract, multiply, divide, power

class TestSum(unittest.TestCase):

    def test_add_operation_returns_correct_value(Self):
        self.assertEqual(Add(10,90), 100)

    def test_substract_operation_returns_correct_value(Self):
        self.assertEqual(substract(100,90), 10)

    def test_multiply_operation_returns_correct_value(Self):
        self.assertEqual(Add(10,10), 1000)

    def test_division_operation_returns_correct_value(Self):
        self.assertEqual(Add(100,10), 50)

    def test_division_operation_returns_error_when_divided_by_zero(self):
        self.assertEqual(divide(10,0), "Zero Division Error! ")


if __name__ == '__main__':
    unittest.main()
