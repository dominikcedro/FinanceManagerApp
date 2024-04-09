"""
original author: Dominik Cedro
created: 2024-04-02
license: GSB 3.0
description: This module contains database_module initialization script using sqlalchemy.
"""
from sqlalchemy import create_engine
from source.database_module.model.base import Base
from source.operations_module.financial_operation import FinOp
from source.database_module.model.finop_model import FinOpModel
from source.database_module.model.categories import Categories
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select

from source.analysis_module.analysis import Analysis

username = 'app'
password = '!675#ap'
host = 'localhost'
database_name = 'financedb'

engine = create_engine(f'mysql://{username}:{password}@{host}/{database_name}')

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()


# cat1 = Categories(id=1,name='Housing', description='Housing expenses')
# cat2 = Categories(id=2, name='groceries', description='Food expenses')
# cat3 = Categories(id=3, name='work', description='Salary')

# exp1 = FinOp(name='Rent', date='2024-03-04 01:00:00', op_type='expense', category=1, value=1000.0)
# exp2 = FinOp(name='Food', date='2024-03-05 01:00:00', op_type='expense', category=2, value=200.0)
# inc1 = FinOp(name='Salary', date='2024-03-06 02:00:00', op_type='income', category=3, value=3000.0)

session.commit()

exp_got = select(FinOpModel).where(FinOpModel.op_type == 'expense')
list_entites = []
with Session() as session:
    for result in session.execute(exp_got):
        # print(result)
        list_entites.append(result)
# print(list_entites)
# print(type(list_entites[0]))

session = Session()
exp = 'expense'
query1 = session.query(FinOpModel).filter(FinOpModel.op_type == exp)

inc = 'income'
query2 = session.query(FinOpModel).filter(FinOpModel.op_type== inc)
expenses = query1.all()
incomes = query2.all()

for entity in expenses:
    print(entity)
for entity in incomes:
    print(entity)

# test analysis - total exp
Test_analysis = Analysis(expenses, incomes)
print(Test_analysis.total_expenses())

# test analysis - date
print(Test_analysis.total_expense_date('2024-03-01 00:00:00', '2024-05-02 23:59:59'))
print(incomes[0].date)


