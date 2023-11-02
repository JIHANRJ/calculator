import unittest
from FCalc import Calculator

class CalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(10, self.calc.add(5, 5), "The addition is wrong")

    def test_subtract(self):
        self.assertEqual(2, self.calc.subtract(4, 2), "Subtraction is wrong")

    def test_multiply(self):
        self.assertEqual(30, self.calc.multiply(10, 3), "Multiplication is wrong")

    def test_divide(self):
        self.assertEqual(2, self.calc.divide(4,2), "Division is wrong")

if __name__ == '__main__':
    unittest.main()

