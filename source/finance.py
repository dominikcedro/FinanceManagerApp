from source.operations_module.financial_operations import Expense, Income, Analyze
program = True

while program:
    num_expenses = int(input('enter number of expenses'))
    expenses = []
    for i in range(num_expenses):
        name = input('enter name')
        date = input('enter date')
        category = input('enter category')
        value = float(input('enter value'))
        expense = Expense(name, date, category, value)
        expenses.append(expense)
    num_incomes = int(input('enter number of incomes'))
    incomes = []
    for i in range(num_incomes):
        name = input('enter name')
        date = input('enter date')
        category = input('enter category')
        value = float(input('enter value'))
        income = Income(name, date, category, value)
        incomes.append(income)
    analyze = Analyze(expenses, incomes)
    print(analyze.total_expenses())
    program = False
