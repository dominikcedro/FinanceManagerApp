"""
original author: Dominik Cedro
created: 2024-04-09
license: BSD 3.0
description: This module contains tests for date_time_calc.py script
"""
import unittest

from source.date_time_calc import is_leap_year
"""
original author: Dominik Cedro
created: 2024-04-11
license: BSD 3.0
description: This module contains tests for my leap year function
"""
class TestLeapYear(unittest.TestCase):
    AVERAGE_LEAP_YEAR = 2024
    AVERAGE_NON_LEAP_YEAR = 2025
    LEAP_YEAR_DIVISIBLE_BY_400 = 2000
    NON_LEAP_YEAR_DIVISIBLE_BY_100 = 2100

    def setUp(self):
        self.test_date_list = [self.AVERAGE_LEAP_YEAR, self.AVERAGE_NON_LEAP_YEAR,
                               self.LEAP_YEAR_DIVISIBLE_BY_400, self.NON_LEAP_YEAR_DIVISIBLE_BY_100]

    def test_positive_leap_average(self):
        self.assertEqual(is_leap_year(self.test_date_list[0]), True)

    def test_negative_leap_average(self):
        self.assertEqual(is_leap_year(self.test_date_list[1]), False)

    def test_positive_leap_400(self):
        self.assertEqual(is_leap_year(self.test_date_list[2]), True)

    def test_negative_leap_100(self):
        self.assertEqual(is_leap_year(self.test_date_list[3]), False)


if __name__ == '__main__':
    unittest.main()