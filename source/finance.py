from source.operations_module.financial_operations import Expense, Income
from source.analysis_module.analysis import Analysis

program = True

# while program:
#     num_expenses = int(input('enter number of expenses'))
#     expenses = []
#     for i in range(num_expenses):
#         name = input('enter name')
#         date = input('enter date')
#         category = input('enter category')
#         value = float(input('enter value'))
#         expense = Expense(name, date, category, value)
#         expenses.append(expense)
#     num_incomes = int(input('enter number of incomes'))
#     incomes = []
#     for i in range(num_incomes):
#         name = input('enter name')
#         date = input('enter date')
#         category = input('enter category')
#         value = float(input('enter value'))
#         income = Income(name, date, category, value)
#         incomes.append(income)
#
#     print(analyze.total_expenses())
#     program = False

exp1 = Expense('Rent', '2022-01-01-12-30', 'Housing', 2000.0)
exp1 = Expense('Repairs', '2022-01-20-12-30', 'Housing', 1000.0)
exp2 = Expense('Groceries', '2022-01-02-12-30', 'Food', 200.0)

inc1 = Income('Salary', '2022-01-01-12-30', 'Job', 3000.0)
inc2 = Income('Freelance', '2022-01-02-12-30', 'Job', 500.0)
inc3 = Income('Gift', '2022-01-03-12-30', 'Other', 100.0)

analyze = Analysis([exp1, exp2], [inc1, inc2, inc3])

print(f' total expenses {analyze.total_expenses()}')
print(f' total incomes {analyze.total_income()}')
print('')
print(f' total expenses for category Housing {analyze.total_expense_category("Housing")}')
print(f' total income for category Job {analyze.total_income_category("Job")}')
print('')
print(f' total expenses for in dates 2022-01-01-00-00 - > 2022-01-02-23-59 {analyze.total_expense_date("2022-01-01-00-00", "2022-01-02-23-59")}')
print(f' total incomes for in dates 2022-01-01-00-00 - > 2022-01-02-23-59 {analyze.total_income_date("2022-01-01-00-00", "2022-01-02-23-59")}')
print()
print("average expenses" , analyze.average_expense())
print("average expenses" , analyze.average_income())
print("average expenses for Housing" , analyze.average_expense_category('Housing'))
