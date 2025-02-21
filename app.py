import unittest
import re

class StringCalculator:
    @staticmethod
    def add(numbers: str) -> int:
        if numbers == "":
            return 0

        delimiter = ","
        if numbers.startswith("//"):
            delimiter, numbers = numbers[2:].split("\n", 1)

        num_list = list(map(int, re.split(f"[{delimiter}\n]", numbers)))
        negatives = [n for n in num_list if n < 0]

        if negatives:
            raise ValueError(f"Negative numbers not allowed: {', '.join(map(str, negatives))}")

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
    def test_custom_delimiter(self):
        self.assertEqual(StringCalculator.add("//;\n1;2"), 3)
    def test_negative_number_exception(self):
        with self.assertRaises(ValueError) as context:
            StringCalculator.add("1,-2,3,-4")
        self.assertEqual(str(context.exception), "Negative numbers not allowed: -2, -4")

if __name__ == "__main__":
    unittest.main()
