# test_math_utils.py
import unittest
from calc import SimpleCalculator
class TestMultiplyFunction(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(SimpleCalculator.multiply(2, 3), 6)  # 2*3 = 6
    def test_negative_numbers(self):
        self.assertEqual(SimpleCalculator.multiply(-2, -4), 8)  # -2*-4 = 8
    def test_positive_and_negative(self):
        self.assertEqual(SimpleCalculator.multiply(3, -5), -15)  # 3*-5 = -15
    def test_zero(self):
        self.assertEqual(SimpleCalculator.multiply(0, 10), 0)  # 0*10 = 0
    def test_with_one(self):
        self.assertEqual(SimpleCalculator.multiply(1, 99), 99)  # 1*99 = 99
# This lets you run the test by executing this file directly
if __name__ == '__main__':
    unittest.main()
