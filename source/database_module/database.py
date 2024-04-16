"""
original author: Dominik Cedro
created: 2024-04-02
license: GSB 3.0
description: This module contains database_module initialization script using sqlalchemy.
"""
import json
from sqlalchemy import create_engine
from source.database_module.model.base import Base
from source.operations_module.financial_operation import FinOp
from source.database_module.model.finop_model import FinOpModel
from source.database_module.model.categories import Categories
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select

from source.analysis_module.analysis import Analysis

with open('database_config.json') as f:
    config = json.load(f)

username = config['username']
password = config['password']
host = config['host']
database_name = config['database_name']

engine = create_engine(f'mysql://{username}:{password}@{host}/{database_name}')

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

#
# cat1 = Categories(id=1, name='Housing', description='Housing expenses')
# cat2 = Categories(id=2, name='groceries', description='Food expenses')
# cat3 = Categories(id=3, name='work', description='Salary')
# #
# session.add(cat1)
# session.add(cat2)
# session.add(cat3)

# cat1 = session.query(Categories).get(1)
# cat2 = session.query(Categories).get(2)
# cat3 = session.query(Categories).get(3)
#
# exp1 = FinOpModel(FinOp(name='Rent', date='2024-03-01 01:00:00', op_type='expense', category=cat1, value=1000.0))
# exp2 = FinOpModel(FinOp(name='Food', date='2024-03-20 01:00:00', op_type='expense', category=cat2, value=200.0))
# inc1 = FinOpModel(FinOp(name='Salary', date='2024-03-06 02:00:00', op_type='income', category=cat3, value=3000.0))
# exp3 = FinOpModel(FinOp(name='Food_more', date='2024-03-05 01:00:00', op_type='expense', category=cat2, value=500.0))
#
# session.add(exp1)
# session.add(exp2)
# session.add(exp3)
# session.add(inc1)
#
# session.commit()



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
print(Test_analysis.total_expense_date('2024-03-01 00:00:00', '2024-03-02 23:59:59'))
print(incomes[0].date)

from source.visualization_module.visualization import Visualization
analysis = Analysis(expenses, [])
visualization = Visualization(analysis)
visualization.plot_total_expenses_month('March')