"""
original author: Dominik Cedro
created: 2024-04-02
license: GSB 3.0
description: This module contains database_module initialization script using sqlalchemy.
"""
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_

from .model.base import Base
from .model.finop_model import FinOpModel
from .model.categories import Categories
from ..analysis_module.analysis import Analysis




def setup_connection_db():

    with open('C:/Users\Domin\PycharmProjects\FinanceManager\source\database_module\database_config.json') as f:
        # what about here, this dir will change?
        config = json.load(f)
    username = config['username']
    password = config['password']
    host = config['host']
    database_name = config['database_name']

    engine = create_engine(f'mysql://{username}:{password}@{host}/{database_name}')

    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    return Session


def query_by_date(Session, date_start, date_end):
    session = Session()
    query = session.query(FinOpModel).filter(and_(FinOpModel.date > date_start, FinOpModel.date < date_end))
    results = query.all()
    return results


def query_by_type(Session, type):
    session = Session()
    query = session.query(FinOpModel).filter(FinOpModel.op_type == type)
    results = query.all()
    return results


Session = setup_connection_db()

if __name__ == "__main__":
    pass

#
#
# # test analysis - total exp
# Test_analysis = Analysis(expenses, incomes)
# print(Test_analysis.total_expenses())
#
# # test analysis - date
# print(Test_analysis.total_expense_date('2024-03-01 00:00:00', '2024-03-02 23:59:59'))
# print(incomes[0].date)
#
# from source.visualization_module.visualization import Visualization
# analysis = Analysis(expenses, [])
# visualization = Visualization(analysis)
# visualization.plot_total_expenses_month('March')