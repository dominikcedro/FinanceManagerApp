"""
original author: Dominik Cedro
created: 2024-03-06
license: BSD 3.0
description: This module contains classes Expense, Income etc. It is a part of a simple personal python finance app.
"""
import unittest
from source.operations_module.financial_operation import FinOp
from source.analysis_module.analysis import Analysis


class TestAnalysis(unittest.TestCase):
    def setUp(self):
        self.exp1 = FinOp('Rent', '2022-03-01 12:30:00', 'expense', 'Housing', 1000.0)
        self.exp2 = FinOp('Groceries', '2022-01-02 12:30:00', 'expense', 'Food', 200.0)
        self.inc1 = FinOp('Salary', '2022-01-01 12:30:00', 'income', 'Job', 3000.0)
        self.analysis = Analysis([self.exp1, self.exp2], [self.inc1])

    def test_total_expenses(self):
        self.assertEqual(self.analysis.total_expenses(), 1200.0)

    def test_total_income(self):
        self.assertEqual(self.analysis.total_income(), 3000.0)

    def test_total_expense_category(self):
        self.assertEqual(self.analysis.total_expense_category('Housing'), 1000.0)

    def test_total_income_category(self):
        self.assertEqual(self.analysis.total_income_category('Job'), 3000.0)

    def test_total_expense_date(self):
        # should return amount for given date starting from 2022-01-01 to 2022-01-02
        self.assertEqual(self.analysis.total_expense_date('2022-01-01 00:00:00', '2022-01-02 23:59:59'), 200.0)

    def test_total_income_date(self):
        # should return amount for given date starting from 2022-01-01 to 2022-01-02
        self.assertEqual(self.analysis.total_income_date('2022-01-01 00:00:00', '2022-01-02 23:59:59'), 3000.0)

    def test_average_expenses(self):
        # should return average expenses per month
        self.assertEqual(self.analysis.average_expense(), 600.0)

    def test_average_income(self):
        # should return average income per month
        self.assertEqual(self.analysis.average_income(), 3000.0)

    def test_average_expense_category(self):
        # should return average expenses for a given category
        self.assertEqual(self.analysis.average_expense_category('Housing'), 500.0)

    def test_average_income_category(self):
        # should return average income for a given category
        self.assertEqual(self.analysis.average_income_category('Job'), 3000.0)


if __name__ == '__main__':
    unittest.main()