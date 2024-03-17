"""
original author: Dominik Cedro
created: 2024-03-06
license: GSB 3.0
description: This module contains classes Expense, Income etc. It is a part of a simple personal python finance app.
"""

# introducing FinOp class


class FinOp:
    def __init__(self, name, date, op_type, category, value):
        self.name = name
        self.date = date
        self.op_type = op_type  # either 'expense' or 'income'
        self.category = category
        self.value = value

    def __str__(self):
        return f'{self.name} - {self.date} - {self.type} - {self.category} - {self.value}'


class Expense(FinOp):
    categories = ['Housing', 'Food', 'Transportation', 'Utilities', 'Insurance',
                  'Medical', 'Savings', 'Debt', 'Entertainment', 'Miscellaneous']

    def __init__(self, name, date, category, value):
        if category not in self.categories:
            raise ValueError('Invalid category')
        super().__init__(name, date, 'expense', category, value)


class Income(FinOp):
    categories = ['Job', 'Investment', 'Gift', 'Other']

    def __init__(self, name, date, category, value):
        if category not in self.categories:
            raise ValueError('Invalid category')
        super().__init__(name, date, 'income', category, value)


class Analyze:
    """
    This class represents a collection of expenses and incomes. It has methods to calculate total expenses, total income,
     and total expenses by category.

     ATTRIBUTES:
    expenses: list of Expense objects
    incomes: list of Income objects

    METHODS:
    total_expenses(): returns the total expenses
    total_income(): returns the total income
    total_expense_category(category): returns the total expenses for a given category
    total_income_category(category): returns the total income for a given category

    """
    def __init__(self, expenses, incomes):
        self.expenses = expenses # should be a list of expenses (from a single reciept)
        self.incomes = incomes # should be a list of incomes (paychecks, other incomes)

    def total_expenses(self):
        return sum(expense.value for expense in self.expenses)

    def total_income(self):
        return sum(income.value for income in self.incomes)

    def total_expense_category(self, category):
        sum = 0
        for expense in self.expenses:
            if expense.category == category:
                sum += expense.value
        return sum

    def total_income_category(self, category):
        sum = 0
        for income in self.incomes:
            if income.category == category:
                sum += income.value
        return sum


    #TODO: add a method to calculate total expenses by date

    #TODO: add a method to calculate total income by date

    #TODO: write unit tests for each method
