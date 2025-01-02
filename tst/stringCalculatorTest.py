import unittest
from src.stringCalculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def test_null_input(self):
        self.assertEqual(StringCalculator.add_numbers(""), 0)

    def test_num_with_delimeter(self):
        self.assertEqual(StringCalculator.add_numbers("1\n2"), 3)
        self.assertEqual(StringCalculator.add_numbers("//;\n1;2"), 3)

    def test_negative_number(self):
        self.assertRaises(ValueError, StringCalculator.add_numbers, "1,-2,3,-4")

if __name__ == "__main__":
    unittest.main()
