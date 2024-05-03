"""
original author: Dominik Cedro
created: 2024-03-06
license: BSD 3.0
description: This module contains classes Expense, Income etc. It is a part of a simple personal python finance app.
"""
import unittest
from source.operations_module.financial_operation import FinOp
from source.analysis_module.analysis import Analysis
import matplotlib
matplotlib.use('Agg')

class TestAnalysis(unittest.TestCase):
    EXPENSE_TYPE = 'expense'
    INCOME_TYPE = 'income'
    HOUSING_CATEGORY = 'Housing'
    FOOD_CATEGORY = 'Food'
    JOB_CATEGORY = 'Job'
    RENT_DATE = '2022-03-01 12:30:00'
    GROCERIES_DATE = '2022-01-02 12:30:00'
    SALARY_DATE = '2022-01-01 12:30:00'
    START_DATE = '2022-01-01 00:00:00'
    END_DATE = '2022-01-02 23:59:59'

    def setUp(self):
        self.exp1 = FinOp('Rent', self.RENT_DATE, self.EXPENSE_TYPE, self.HOUSING_CATEGORY, 1000.0)
        self.exp2 = FinOp('Groceries', self.GROCERIES_DATE, self.EXPENSE_TYPE, self.FOOD_CATEGORY, 200.0)
        self.inc1 = FinOp('Salary', self.SALARY_DATE, self.INCOME_TYPE, self.JOB_CATEGORY, 3000.0)
        self.analysis = Analysis([self.exp1, self.exp2], [self.inc1])

    def test_total_expenses(self):
        self.assertEqual(self.analysis.total_expenses(), 1200.0)

    def test_total_income(self):
        self.assertEqual(self.analysis.total_income(), 3000.0)

    # def test_total_expense_category(self):
    #     self.assertEqual(self.analysis.total_expense_category(self.HOUSING_CATEGORY), 1000.0)

    def test_total_income_category(self):
        self.assertEqual(self.analysis.total_income_category(self.JOB_CATEGORY), 3000.0)

    def test_total_expense_date(self):
        self.assertEqual(self.analysis.total_expense_date(self.START_DATE, self.END_DATE), 200.0)

    def test_total_income_date(self):
        self.assertEqual(self.analysis.total_income_date(self.START_DATE, self.END_DATE), 3000.0)

    def test_average_expenses(self):
        self.assertEqual(self.analysis.average_expense(), 600.0)

    def test_average_income(self):
        self.assertEqual(self.analysis.average_income(), 3000.0)

    def test_average_expense_category(self):
        self.assertEqual(self.analysis.average_expense_category(self.HOUSING_CATEGORY), 500.0)

    def test_average_income_category(self):
        self.assertEqual(self.analysis.average_income_category(self.JOB_CATEGORY), 3000.0)


if __name__ == '__main__':
    unittest.main()
