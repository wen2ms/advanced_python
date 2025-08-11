from calculator import Calculator
import unittest

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(1, 2), 3)
    
    def test_add_negative(self):
        self.assertEqual(Calculator.add(-1, -2), -3)