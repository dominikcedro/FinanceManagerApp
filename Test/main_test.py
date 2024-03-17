import unittest
from Source.FinancialOperations.main import Expense, Income, Analyze

class TestAnalyze(unittest.TestCase):
    def setUp(self):
        self.exp1 = Expense('Rent', '2022-01-01', 'Housing', 1000.0)
        self.exp2 = Expense('Groceries', '2022-01-02', 'Food', 200.0)
        self.inc1 = Income('Salary', '2022-01-01', 'Job', 3000.0)
        self.analyze = Analyze([self.exp1, self.exp2], [self.inc1])

    def test_total_expenses(self):
        self.assertEqual(self.analyze.total_expenses(), 1200.0)

    def test_total_income(self):
        self.assertEqual(self.analyze.total_income(), 3000.0)

    def test_total_expense_category(self):
        self.assertEqual(self.analyze.total_expense_category('Housing'), 1000.0)


if __name__ == '__main__':
    unittest.main()