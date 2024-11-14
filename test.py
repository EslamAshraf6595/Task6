import unittest
from calclutor import calc
class TestCalculator(unittest.TestCase):
    def test_add(self):
        result =calc.add(2,2)
        self.assertEqual(result,4)
if __name__== '__main__':
    unittest.main
