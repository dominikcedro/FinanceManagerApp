"""
original author: Dominik Cedro
created: 2024-03-17
license: BSD 3.0
description: This module contains tests for the financial_operations module for my python finance app.
"""
import unittest
from source.operations_module.financial_operation import FinOp


class TestFinOp(unittest.TestCase):

    INCORRECT_TYPE = 1
    INCORRECT_DATE = 2
    INCORRECT_OP_TYPE = 1.0
    INCORRECT_VALUE = "1.0"
    VALUE_EQUAL_ZERO = 0.0
    VALUE_SMALLER_ZERO = -100.0

    def setUp(self):
        self.exp1 = FinOp('Rent', '2022-01-01 00:00:00', 'expense', 'Housing', 1000.0)
        self.exp2 = FinOp('Groceries', '2022-01-02 00:00:00', 'expense', 'Food', 200.0)
        self.inc1 = FinOp('Salary', '2022-01-01 00:00:00', 'income', 'Job', 3000.0)

    def test_name_type_check(self):
        with self.assertRaises(ValueError):
            FinOp(self.INCORRECT_TYPE, '2022-01-01 00:00:00', 'expense', 'Housing', 1000.0)

    def test_date_type_check(self):
        with self.assertRaises(ValueError):
            FinOp("Rent", self.INCORRECT_DATE, 'expense', 'Housing', 1000.0)

    def test_op_type_type_check(self):
        with self.assertRaises(ValueError):
            FinOp('Rent', '2022-01-01 00:00:00', self.INCORRECT_OP_TYPE, 'Housing', 1000.0)

    # def test_category_type_check(self):
    #     with self.assertRaises(ValueError):
    #         FinOp('Rent', '2022-01-01 00:00:00', 'expense', 1.0, 1000.0)

    def test_value_type_check(self):
        with self.assertRaises(ValueError):
            FinOp('Rent', '2022-01-01 00:00:00', 'expense', 'Housing', self.INCORRECT_VALUE)

    def test_value_value_check(self):
        with self.assertRaises(ValueError):
            FinOp('Rent', '2022-01-01 00:00:00', 'expense', 'Housing', self.VALUE_EQUAL_ZERO)
        with self.assertRaises(ValueError):
            FinOp('Rent', '2022-01-01 00:00:00', 'expense', 'Housing', self.VALUE_SMALLER_ZERO)

    def test_str(self):
        self.assertEqual(str(self.exp1), 'Rent - 2022-01-01 00:00:00 - expense - Housing - 1000.0')
        self.assertEqual(str(self.inc1), 'Salary - 2022-01-01 00:00:00 - income - Job - 3000.0')


if __name__ == '__main__':
    unittest.main()
