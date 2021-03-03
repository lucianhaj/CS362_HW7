import unittest
import FizzBuzz


class TestFizzBuzz(unittest.TestCase):

    def test_normal(self):
        self.assertEqual(FizzBuzz.fizznbuzz(1), 1)
        self.assertEqual(FizzBuzz.fizznbuzz(4), 4)
        self.assertEqual(FizzBuzz.fizznbuzz(100), 100)


if __name__ == "__main__":
    unittest.main()


