"""
original author: Dominik Cedro
created: 2024-03-17
license: BSD 3.0
description: This module contains tests for the financial_operations module for my python finance app.
"""
import unittest
from source.operations_module.financial_operation import FinOp


class TestFinOp(unittest.TestCase):
    def setUp(self):
        self.exp1 = FinOp('Rent', '2022-01-01 00:00:00', 'expense', 'Housing', 1000.0)
        self.exp2 = FinOp('Groceries', '2022-01-02 00:00:00', 'expense', 'Food', 200.0)
        self.inc1 = FinOp('Salary', '2022-01-01 00:00:00', 'income', 'Job', 3000.0)

    def test_name_type_check(self):
        with self.assertRaises(ValueError):
            FinOp(1, '2022-01-01 00:00:00', 'expense', 'Housing', 1000.0)

    def test_date_type_check(self):
        with self.assertRaises(ValueError):
            FinOp("Rent", 2, 'expense', 'Housing', 1000.0)

    def test_op_type_type_check(self):
        with self.assertRaises(ValueError):
            FinOp('Rent', '2022-01-01 00:00:00', 1.0, 'Housing', 1000.0)

    # def test_category_type_check(self):
    #     with self.assertRaises(ValueError):
    #         FinOp('Rent', '2022-01-01 00:00:00', 'expense', 1.0, 1000.0)

    def test_value_type_check(self):
        with self.assertRaises(ValueError):
            FinOp('Rent', '2022-01-01 00:00:00', 'expense', 'Housing', "00")

    def test_value_value_check(self):
        # check if value <= 0 raises an error
        with self.assertRaises(ValueError):
            FinOp('Rent', '2022-01-01 00:00:00', 'expense', 'Housing', 0.0)        # check if value <= 0 raises an error
        with self.assertRaises(ValueError):
            FinOp('Rent', '2022-01-01 00:00:00', 'expense', 'Housing', -1000.0)

    def test_str(self):
        self.assertEqual(str(self.exp1), 'Rent - 2022-01-01 00:00:00 - expense - Housing - 1000.0')
        self.assertEqual(str(self.inc1), 'Salary - 2022-01-01 00:00:00 - income - Job - 3000.0')


if __name__ == '__main__':
    unittest.main()