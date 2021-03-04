import unittest
import LeapYear


class TestLeapYear(unittest.TestCase):

    def test_divisible_by_four(self):
        self.assertEqual(LeapYear_TDD.leap(4), "Leap Year!")
        self.assertEqual(LeapYear_TDD.leap(16), "Leap Year!")
        self.assertEqual(LeapYear_TDD.leap(24), "Leap Year!")
        self.assertEqual(LeapYear_TDD.leap(2), "Not a Leap Year!")
        self.assertEqual(LeapYear_TDD.leap(0), "Not a Leap Year!")






if __name__ == "__main__":
    unittest.main()
