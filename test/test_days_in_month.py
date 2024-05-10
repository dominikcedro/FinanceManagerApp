"""
original author: Dominik Cedro
created: 2024-04-09
license: BSD 3.0
description: This module contains tests for date_time_calc.py script
"""
import unittest

from source.common.date_time_calc import days_in_month


class DaysInMonth(unittest.TestCase):
    JANUARY = 1
    FEBRUARY = 2
    INVALID_MONTH_LOW = 0
    INVALID_MONTH_HIGH = 13
    INVALID_MONTH_STRING = "March"
    LEAP_YEAR = True
    NON_LEAP_YEAR = False

    def setUp(self):
        self.test_list = [(self.JANUARY, self.LEAP_YEAR), (self.JANUARY, self.NON_LEAP_YEAR),
                          (self.FEBRUARY, self.LEAP_YEAR), (self.FEBRUARY, self.NON_LEAP_YEAR),
                          (self.INVALID_MONTH_LOW, self.LEAP_YEAR), (self.INVALID_MONTH_HIGH, self.LEAP_YEAR),
                          (self.INVALID_MONTH_STRING, self.LEAP_YEAR)]

    def test_january(self):
        self.assertEqual(days_in_month(self.test_list[0][0], self.test_list[0][1]), 31)

    def test_january_2(self):
        self.assertEqual(days_in_month(self.test_list[1][0], self.test_list[1][1]), 31)

    def test_february_leap(self):
        self.assertEqual(days_in_month(self.test_list[2][0], self.test_list[2][1]), 29)

    def test_february_no_leap(self):
        self.assertEqual(days_in_month(self.test_list[3][0], self.test_list[3][1]), 28)

    def test_border_month_0(self):
        with self.assertRaises(ValueError):
            days_in_month(self.test_list[4][0], self.test_list[4][1])

    def test_border_month_13(self):
        with self.assertRaises(ValueError):
            days_in_month(self.test_list[5][0], self.test_list[5][1])

    def test_type_error_string(self):
        with self.assertRaises(TypeError):
            days_in_month(self.test_list[6][0], self.test_list[6][1])


if __name__ == '__main__':
    unittest.main()
