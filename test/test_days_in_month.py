"""
original author: Dominik Cedro
created: 2024-04-09
license: BSD 3.0
description: This module contains tests for date_time_calc.py script
"""
import unittest

from source.date_time_calc import days_in_month

class DaysInMonth(unittest.TestCase):
    def setUp(self):
        self.test_list = [(1, True), (1, False), (2, True),
                          (2, False), (0, True), (13, True),
                          ("March", True)]
    def test_january(self):
        self.assertEqual(days_in_month(self.test_list[0][0],self.test_list[0][1]), 31)

    def test_january_2(self):
        self.assertEqual(days_in_month(self.test_list[1][0], self.test_list[1][1]), 31)

    def test_february_leap(self):
        self.assertEqual(days_in_month(self.test_list[2][0], self.test_list[2][1]), 29)

    def test_february_no_leap(self):
        self.assertEqual(days_in_month(self.test_list[3][0], self.test_list[3][1]), 28)

    def test_border_month_0(self):
        self.assertEqual(days_in_month(self.test_list[4][0], self.test_list[4][1]), ValueError)

    def test_border_month_13(self):
        self.assertEqual(days_in_month(self.test_list[5][0], self.test_list[5][1]), ValueError)

    def test_type_error_string(self):
        self.assertEqual(days_in_month(self.test_list[6][0], self.test_list[6][1]), TypeError)


if __name__ == '__main__':
    unittest.main()