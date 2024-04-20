"""
original author: Dominik Cedro
created: 2024-04-17
license: GSB 3.0
description: This module main app functionalities
"""

from source.database_module.database import setup_connection_db, query_by_date, query_by_type
from source.database_module.model.finop_model import FinOpModel
from source.operations_module.financial_operation import FinOp
from source.analysis_module.analysis import Analysis
from source.visualization_module.visualization import Visualization
from source.database_module.model.categories import Categories

## tutaj będzie sobie wybierał co trzeba w danej chwili
session = setup_connection_db()
list_of_queried_date = query_by_date(session, '2022-01-01 00:00:00', '2025-12-01 00:00:00')

for x in list_of_queried_date:
    print(x)

analysis = Analysis(list_of_queried_date, [])
visualization = Visualization(analysis)
visualization.plot_total_expenses_month('March')

with session() as session:
    category = session.query(Categories).filter(Categories.name == "groceries").first()

    new_expense = FinOpModel(FinOp('even more groceries', '2022-03-12 00:00:00', 'expense', category, 150.0))
    # session.add(new_expense)

    session.commit()
