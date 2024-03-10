

class Expense:
    """
    This class represents an expense. It has a name, date, category, and value.

    ATTRIBUTES:
    name: str
    date: str
    category: str
    value: float

    METHODS:
    __init__(name, date, category, value)
    __str__(): returns a string representation of the expense
    
    """
    def __init__(self, name, date, category, value):
        self.name = name
        self.date = date
        self.category = category
        self.value = value

    def __str__(self):
        return f'{self.name} - {self.date} - {self.category} - {self.value}'


class Income:
    def __init__(self, name, date, category, value):
        self.name = name
        self.date = date
        self.category = category
        self.value = value

    def __str__(self):
        return f'{self.name} - {self.date} - {self.category} - {self.value}'


class Analyze:
    def __init__(self, expenses, incomes):
        self.expenses = expenses # should be a list of expenses (from a single reciept)
        self.incomes = incomes # should be a list of incomes (paychecks, other incomes)

        def total_expenses(self):
            return sum(expense.value for expense in self.expenses)

