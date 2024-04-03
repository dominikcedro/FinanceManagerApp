"""
original author: Dominik Cedro
created: 2024-04-02
license: GSB 3.0
description: This module contains database initialization script using sqlalchemy.
"""
from source.operations_module.categories import Categories
from source.operations_module.financial_operations import Expense, Income
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from source.operations_module.base import Base



engine = create_engine('mySQL+mysqldb://root:Calathea137!@localhost/financedb')

Base.metadata.create_all(bind=engine)

# Session = sessionmaker(bind=engine)
# session = Session()
#
# # exp1 = Expense('Rent', '2022-01-01-12-30', 1, 1000.0)
# # session.add(exp1)
# inc1 = Income('Salary', '2022-01-01-12-30', 1, 3000.0)
# session.add(inc1)
# session.commit()