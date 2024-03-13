

class Expense:
    """
    This class represents a single expense. It has a name, date, category, and value.

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

    #TODO: add a method to calculate total expenses by category

    #TODO: add a method to calculate total expenses by date

    #TODO: add a method to calculate total income by date

    #TODO: add a method to calculate total income by category

    #TODO: write unit tests for each method
