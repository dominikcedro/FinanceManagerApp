"""
original author: Dominik Cedro
created: 2024-03-17
license: BSD 3.0
description: This module contains classes analysis_module. It is a part of a simple personal python finance app.
"""
from datetime import datetime

DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'

class Analysis:
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
    total_expense_date(start_date, end_date): returns the total expenses for a given date range
    total_income_date(start_date, end_date): returns the total income for a given date range
    """

    def __init__(self, expenses, incomes):
        self.expenses = expenses
        self.incomes = incomes
        self.datetime_format = DATETIME_FORMAT

    def total_expenses(self):
        return round(sum(expense.value for expense in self.expenses),2)

    def total_income(self):
        return round(sum(income.value for income in self.incomes),2)

    def total_expense_category(self, category):
        sum = 0
        for expense in self.expenses:
            if expense.category.name == category:
                sum += expense.value
        return sum

    def total_income_category(self, category):
        sum = 0
        for income in self.incomes:
            if income.category == category:
                sum += income.value
        return sum

    def total_expense_date(self, start_date, end_date):
        start_date = datetime.strptime(start_date, self.datetime_format)
        end_date = datetime.strptime(end_date, self.datetime_format)

        sum = 0
        for expense in self.expenses:
            if start_date <= expense.date <= end_date:
                sum += expense.value
        return sum

    def total_income_date(self, start_date, end_date):
        start_date = datetime.strptime(start_date, self.datetime_format)
        end_date = datetime.strptime(end_date, self.datetime_format)

        sum = 0
        for income in self.incomes:
            if start_date <= income.date <= end_date:
                sum += income.value
        return sum

    def average_income(self):
        return round(self.total_income() / len(self.incomes),2)

    def average_expense(self):
        return round(self.total_expenses() / len(self.expenses),2)

    def average_expense_category(self, category):
        return self.total_expense_category(category) / len(self.expenses)

    def average_income_category(self, category):
        return self.total_income_category(category) / len(self.incomes)
