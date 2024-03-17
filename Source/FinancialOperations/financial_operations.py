"""
original author: Dominik Cedro
created: 2024-03-06
license: GSB 3.0
description: This module contains classes Expense, Income etc. It is a part of a simple personal python finance app.
"""


class FinOp:
    """
    This class represents a single financial operation. It is a parent class for Expense and Income classes.

    ATTRIBUTES:
    name: str
    date: str
    op_type: str
    category: str
    value: float

    METHODS:
    __str__(): returns a string representation of the object

    """
    def __init__(self, name, date, op_type, category, value):
        self.name = name
        self.date = date
        self.op_type = op_type  # either 'expense' or 'income'
        self.category = category
        self.value = value

    def __str__(self):
        return f'{self.name} - {self.date} - {self.type} - {self.category} - {self.value}'


class Expense(FinOp):
    """
    This class represents a single expense. It is a child class of FinOp.

    ATTRIBUTES:
    categories: list of str

    """
    categories = ['Housing', 'Food', 'Transportation', 'Utilities', 'Insurance',
                  'Medical', 'Savings', 'Debt', 'Entertainment', 'Miscellaneous']

    def __init__(self, name, date, category, value):
        if category not in self.categories:
            raise ValueError('Invalid category')
        super().__init__(name, date, 'expense', category, value)


class Income(FinOp):
    """
    This class represents a single income. It is a child class of FinOp.

    ATTRIBUTES:
    categories: list of str

    """
    categories = ['Job', 'Investment', 'Gift', 'Other']

    def __init__(self, name, date, category, value):
        if category not in self.categories:
            raise ValueError('Invalid category')
        super().__init__(name, date, 'income', category, value)

