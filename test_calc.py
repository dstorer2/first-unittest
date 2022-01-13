import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(15, -5), 10)
        self.assertEqual(calc.add(-5, 5), 0)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(15, -5), 20)
        self.assertEqual(calc.subtract(-5, 5), -10)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(15, -5), -75)
        self.assertEqual(calc.multiply(-5, -5), 25)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(15, -5), -3)
        self.assertEqual(calc.divide(-5, 5), -1)

if __name__ == '__main__':
    unittest.main()