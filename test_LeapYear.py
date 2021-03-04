import unittest
import LeapYear


class TestLeapYear(unittest.TestCase):

    def test_divisible_by_four(self):
        self.assertEqual(LeapYear.leap(4), "Leap Year!")
        self.assertEqual(LeapYear.leap(16), "Leap Year!")
        self.assertEqual(LeapYear.leap(24), "Leap Year!")
        self.assertEqual(LeapYear.leap(2), "Not a Leap Year!")
        self.assertEqual(LeapYear.leap(0), "Not a Leap Year!")

    def test_divisible_by_100(self):
        self.assertEqual(LeapYear.leap(1000), "Not a Leap Year!")
        self.assertEqual(LeapYear.leap(8), "Leap Year!")
        self.assertEqual(LeapYear.leap(4), "Leap Year!")
        self.assertEqual(LeapYear.leap(100), "Not a Leap Year!")
        self.assertEqual(LeapYear.leap(255), "Not a Leap Year!")

    def test_divisible_by_400(self):
        self.assertEqual(LeapYear.leap(2000), "Leap Year!")
        self.assertEqual(LeapYear.leap(400), "Leap Year!")
        self.assertEqual(LeapYear.leap(2012), "Leap Year!")
        self.assertEqual(LeapYear.leap(1000), "Not a Leap Year!")
        self.assertEqual(LeapYear.leap(500), "Not a Leap Year!")
        self.assertEqual(LeapYear.leap(200), "Not a Leap Year!")






if __name__ == "__main__":
    unittest.main()
