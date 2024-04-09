"""
original author: Dominik Cedro
created: 2024-04-09
license: BSD 3.0
description: This module contains tests for date_time_calc.py script
"""
import unittest

from source.date_time_calc import is_leap_year
#This extra leap day occurs in each year that is a multiple of 4,
# except for years evenly divisible by 100 but not by 400.

class TestDateTimeCalc(unittest.TestCase):
    def setUp(self):
        self.test_date_list = ["2024-06-01 10:11:11", "2025-06-01 10:11:11",
                               "2000-06-01 10:11:11", "2100-06-01 10:11:11",
                               "20241-06-10 10:10:11"]
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