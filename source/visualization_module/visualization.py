"""
original author: Dominik Cedro
created: 2024-03-27
license: BSD 3.0
description: This module contains visalization class for python finance app.
"""

import matplotlib.pyplot as plt
from source.analysis_module.analysis import Analysis
from source.operations_module.financial_operations import Expense, Income

class Visualization:

    def __init__(self, analysis):
        self.analysis = analysis
        self.list_of_months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
                          'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}

    # TODO plot total expenses in given month (amount in frequency)
    # TODO plot expenses by category in a given month
    # TODO same for incomes
    def plot_total_expenses_month(self, month_name: str):

        if month_name not in self.list_of_months:
            raise ValueError('Invalid month')
        month = self.list_of_months[month_name]

        # Filter expenses for the given month
        expenses_in_month = [expense for expense in self.analysis.expenses if expense.date.month == month]

        # Extract day and value for each expense in the month
        days = [expense.date.day for expense in expenses_in_month]
        values = [expense.value for expense in expenses_in_month]

        plt.figure(figsize=(10, 5))
        plt.bar(days, values)
        plt.xlabel('Day of the month')
        plt.ylabel('Total expenses ($)')
        plt.title(f'Total expenses in {month_name}')
        plt.xticks(range(1, len(days)+1))
        plt.show()

    def plot_expenses_month_frequency(self, month_name: str):

            if month_name not in self.list_of_months:
                raise ValueError('Invalid month')
            month = self.list_of_months[month_name]

            # Filter expenses for the given month and category
            expenses_in_month = [expense for expense in self.analysis.expenses if
                                 expense.date.month == month]

            # Extract day and value for each expense in the month
            days = [expense.date.day for expense in expenses_in_month]
            expense_counts = {day: 0 for day in range(1, 32)}

            for expense in expenses_in_month:
                day = expense.date.day
                expense_counts[day] += 1
            counts = list(expense_counts.values())

            plt.figure(figsize=(10, 5))
            plt.bar(days, counts)
            plt.xlabel('Day of the month')
            plt.ylabel('Number of expenses')
            plt.title(f'Number of expenses in {month_name}')
            plt.xticks(range(1, 32))  # Set x-axis ticks to be every day of the month
            plt.show()