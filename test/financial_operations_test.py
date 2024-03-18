"""
original author: Dominik Cedro
created: 2024-03-17
license: GSB 3.0
description: This module contains tests for the financial_operations module for my python finance app.
"""

import unittest
from source.operations_module.financial_operations import Expense, Income
from source.analysis_module.analysis import Analysis


class TestFinOp(unittest.TestCase):
    def setUp(self):
        self.exp1 = Expense('Rent', '2022-01-01-00-00', 'Housing', 1000.0)
        self.exp2 = Expense('Groceries', '2022-01-02-00-00', 'Food', 200.0)
        self.inc1 = Income('Salary', '2022-01-01-00-00', 'Job', 3000.0)

    def test_name_type_check(self):
        with self.assertRaises(ValueError):
            Expense(1, '2022-01-01', 'Housing', 1000.0)

    def test_date_type_check(self):
        with self.assertRaises(ValueError):
            Expense('Rent', 1, 'Housing', 1000.0)

    def test_op_type_type_check(self):
        with self.assertRaises(ValueError):
            Expense('Rent', '2022-01-01', 1, 1000.0)

    def test_category_type_check(self):
        with self.assertRaises(ValueError):
            Expense('Rent', '2022-01-01', 1, 1000.0)

    def test_value_type_check(self):
        with self.assertRaises(ValueError):
            Expense('Rent', '2022-01-01', 'Housing', '1000.0')

    def test_value_value_check(self):
        # check if value <= 0 raises an error
        with self.assertRaises(ValueError):
            Expense('Rent', '2022-01-01', 'Housing', 0.0)
        # check if value <= 0 raises an error
        with self.assertRaises(ValueError):
            Expense('Rent', '2022-01-01', 'Housing', -1000.0)

    def test_str(self):
        self.assertEqual(str(self.exp1), 'Rent - 2022-01-01 00:00:00 - expense - Housing - 1000.0')
        self.assertEqual(str(self.inc1), 'Salary - 2022-01-01 00:00:00 - income - Job - 3000.0')




