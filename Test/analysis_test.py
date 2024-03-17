"""
original author: Dominik Cedro
created: 2024-03-06
license: GSB 3.0
description: This module contains classes Expense, Income etc. It is a part of a simple personal python finance app.
"""

import unittest
from Source.FinancialOperations.financial_operations import Expense, Income
from Source.Analysis.analysis import Analysis


class TestAnalyze(unittest.TestCase):
    def setUp(self):
        self.exp1 = Expense('Rent', '2022-01-01', 'Housing', 1000.0)
        self.exp2 = Expense('Groceries', '2022-01-02', 'Food', 200.0)
        self.inc1 = Income('Salary', '2022-01-01', 'Job', 3000.0)
        self.analyze = Analysis([self.exp1, self.exp2], [self.inc1])

    def test_total_expenses(self):
        self.assertEqual(self.analyze.total_expenses(), 1200.0)

    def test_total_income(self):
        self.assertEqual(self.analyze.total_income(), 3000.0)

    def test_total_expense_category(self):
        self.assertEqual(self.analyze.total_expense_category('Housing'), 1000.0)


if __name__ == '__main__':
    unittest.main()