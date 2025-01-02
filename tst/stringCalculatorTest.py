import unittest
from src.stringCalculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def test_null_input(self):
        self.assertEqual(StringCalculator.add_numbers(""), 0)

if __name__ == "__main__":
    unittest.main()
