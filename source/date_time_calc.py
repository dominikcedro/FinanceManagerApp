"""
original author: Dominik Cedro
created: 2024-04-11
license: BSD 3.0
description: This module contains my leap year handling logic
"""


def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def days_in_month(int_month: int, is_leap: bool):
    if not isinstance(int_month, int):
        raise TypeError('Invalid month integer')
    if not isinstance(is_leap, bool):
        raise ValueError('Invalid is_leap')
    if int_month < 1 or int_month > 12:
        raise ValueError('Month integer must be lower than 12, higher than 0')

    dict_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                  7: 31, 8: 31, 9: 30, 10: 31, 11: 0, 12: 31}
    if is_leap:
        dict_month[2] = 29
    return dict_month[int_month]
