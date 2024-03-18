"""
original author: Dominik Cedro
created: 2024-03-17
license: GSB 3.0
description: This module contains classes analysis_module. It is a part of a simple personal python finance app.
"""
from datetime import datetime


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

    def total_expense_date(self, start_date, end_date):
        start_date = datetime.strptime(start_date, '%Y-%m-%d-%H-%M')
        end_date = datetime.strptime(end_date, '%Y-%m-%d-%H-%M')

        sum = 0
        for expense in self.expenses:
            if start_date <= expense.date <= end_date:
                sum += expense.value
        return sum

    def total_income_date(self, start_date, end_date):
        start_date = datetime.strptime(start_date, '%Y-%m-%d-%H-%M')
        end_date = datetime.strptime(end_date, '%Y-%m-%d-%H-%M')

        sum = 0
        for income in self.incomes:
            if start_date <= income.date <= end_date:
                sum += income.value
        return sum
