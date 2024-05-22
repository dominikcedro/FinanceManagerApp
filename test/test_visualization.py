"""
original author: Dominik Cedro
created: 2024-04-15
license: BSD 3.0
description: This module contains visualization class tests
"""

import unittest
from source.operations.financial_operation import FinOp
from source.analysis.analysis import Analysis
from source.visualization.visualization import Visualization


class TestFinOp(unittest.TestCase):

    CORRECT_MONTH_NAME = "January"
    INCORRECT_MONTH_NAME = "Januarary"
    INCORRECT_MONTH_TYPE = 1
    MONTH_WITH_NO_INCOMES = "March"

    def setUp(self):
        self.exp1 = FinOp('Rent', '2022-01-01 00:00:00', 'expense', 'Housing', 1000.0)
        self.exp2 = FinOp('Groceries', '2022-01-02 00:00:00', 'expense', 'Food', 200.0)
        self.inc1 = FinOp('Salary', '2022-01-01 00:00:00', 'income', 'Job', 3000.0)
        self.analysis = Analysis([self.exp1, self.exp2], [self.inc1])

    def test_correct_month_name(self):
        visualization = Visualization(self.analysis)
        self.assertEqual(None, visualization.plot_total_expenses_month(self.CORRECT_MONTH_NAME))

    def test_incorrect_month_name(self):
        with self.assertRaises(ValueError):
            visualization = Visualization(self.analysis)
            visualization.plot_total_expenses_month(self.INCORRECT_MONTH_NAME)

    # def test_incorrect_month_type(self):
    #     with self.assertRaises(TypeError):
    #         visualization = Visualization(self.analysis)
    #         visualization.plot_total_expenses_month(self.INCORRECT_MONTH_TYPE)


if __name__ == '__main__':
    unittest.main()
