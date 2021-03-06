import unittest
import FizzBuzz


class TestFizzBuzz(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(FizzBuzz.fizznbuzz(1), 1)
        self.assertEqual(FizzBuzz.fizznbuzz(4), 4)
    def test_fizz(self):
        self.assertEqual(FizzBuzz.fizznbuzz(3), "Fizz")
        self.assertEqual(FizzBuzz.fizznbuzz(6), "Fizz")

    def test_buzz(self):
        self.assertEqual(FizzBuzz.fizznbuzz(5), "Buzz")
        self.assertEqual(FizzBuzz.fizznbuzz(10), "Buzz")

    def test_fizz_and_buzz(self):
        self.assertEqual(FizzBuzz.fizznbuzz(15), "FizzBuzz")
        self.assertEqual(FizzBuzz.fizznbuzz(30), "FizzBuzz")














if __name__ == "__main__":
    unittest.main()


