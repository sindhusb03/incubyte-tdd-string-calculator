import unittest
import re

class StringCalculator:
    @staticmethod
    def add(numbers: str) -> int:
        if numbers == "":
            return 0
        num_list = list(map(int, re.split(",|\n", numbers)))
        return sum(num_list)

class TestStringCalculator(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(StringCalculator.add(""), 0)
    def test_single_number(self):
        self.assertEqual(StringCalculator.add("1"), 1)
    def test_two_numbers(self):
        self.assertEqual(StringCalculator.add("1,5"), 6)
    def test_multiple_numbers(self):
        self.assertEqual(StringCalculator.add("1,2,3,4"), 10)
    def test_newline_as_delimiter(self):
        self.assertEqual(StringCalculator.add("1\n2,3"), 6)


if __name__ == "__main__":
    unittest.main()
