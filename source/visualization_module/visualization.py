"""
original author: Dominik Cedro
created: 2024-03-27
license: BSD 3.0
description: This module contains visalization class for python finance app.
"""

import matplotlib.pyplot as plt
from source.analysis_module.analysis import Analysis
from source.operations_module.financial_operation import FinOp
from source.date_time_calc import is_leap_year, days_in_month


class Visualization:

    def __init__(self, analysis):
        self.analysis = analysis

        self.list_of_months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
                               'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}

    def plot_total_expenses_and_incomes_month(self, month_name: str):
        if month_name not in self.list_of_months:
            raise ValueError('Invalid month')

        month = self.list_of_months[month_name]

        # Filter expenses and incomes for the given month
        expenses_in_month = [expense for expense in self.analysis.expenses if expense.date.month == month]
        incomes_in_month = [income for income in self.analysis.incomes if income.date.month == month]

        # Get the days and values for expenses and incomes
        expense_days = [expense.date.day for expense in expenses_in_month]
        expense_values = [-expense.value for expense in expenses_in_month]  # make expense values negative
        income_days = [income.date.day for income in incomes_in_month]
        income_values = [income.value for income in incomes_in_month]

        # Get the maximum number of days in the month
        year = expenses_in_month[0].date.year if expenses_in_month else incomes_in_month[0].date.year
        max_days = days_in_month(self.list_of_months[month_name], is_leap_year(year))

        plt.figure(figsize=(10, 5))

        # Plot expenses and incomes
        plt.bar(expense_days, expense_values, color='red', label='Expenses')
        plt.bar(income_days, income_values, color='green', label='Incomes')

        plt.xlabel('Day of the month')
        plt.ylabel('Total expenses/incomes ($)')
        plt.title(f'Total expenses and incomes in {month_name}')
        plt.xlim(0, max_days + 1)
        plt.xticks(range(1, max_days + 1))
        plt.legend()  # add a legend to distinguish expenses and incomes
        plt.axhline(0, color='black')  # add x-axis in the middle of the plot

        plt.show()
        return None

    def plot_total_expenses_month(self, month_name: str):

        if month_name not in self.list_of_months:
            raise ValueError('Invalid month')

        month = self.list_of_months[month_name]

        # Filter expenses for the given month
        expenses_in_month = [expense for expense in self.analysis.expenses if expense.date.month == month]
        # if month is empty just return message "empty", not error

        values = [expense.value for expense in expenses_in_month]
        days = [expense.date.day for expense in expenses_in_month]

        # I will get the days from my functions based on datetime year
        year = expenses_in_month[0].date.year
        max_days = days_in_month(self.list_of_months[month_name], is_leap_year(year))

        plt.figure(figsize=(10, 5))
        plt.bar(days, values)
        plt.xlabel('Day of the month')
        plt.ylabel('Total expenses ($)')
        plt.title(f'Total expenses in {month_name}')
        plt.xlim(0, max_days + 1)
        plt.xticks(range(1, max_days + 1))

        plt.show()
        return None

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
