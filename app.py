import unittest

class StringCalculator:
    @staticmethod
    def add(numbers: str) -> int:
        if numbers == "":
            return 0
        return int(numbers)


class TestStringCalculator(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(StringCalculator.add(""), 0)
    def test_single_number(self):
        self.assertEqual(StringCalculator.add("1"), 1)


if __name__ == "__main__":
    unittest.main()
