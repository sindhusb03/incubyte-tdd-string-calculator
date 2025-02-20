import unittest

class StringCalculator:
    @staticmethod
    def add(numbers: str) -> int:
        if numbers == "":
            return 0
        num_list = list(map(int, numbers.split(",")))
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

if __name__ == "__main__":
    unittest.main()
