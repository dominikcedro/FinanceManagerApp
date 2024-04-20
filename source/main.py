"""
original author: Dominik Cedro
created: 2024-04-17
license: GSB 3.0
description: This module main app functionalities
"""
import argparse
from .database_module.database import setup_connection_db, query_by_date, query_by_type
from .database_module.model.finop_model import FinOpModel
from .operations_module.financial_operation import FinOp
from .analysis_module.analysis import Analysis
from .visualization_module.visualization import Visualization
from .database_module.model.categories import Categories
def main():

    parser = argparse.ArgumentParser(description="Python Finance App")

    subparsers = parser.add_subparsers(dest="command")

    # Add financial operation command
    add_parser = subparsers.add_parser('add_op', help='Add a new financial operation to the database')
    add_parser.add_argument('name_op', type=str, help='Name of the operation')
    add_parser.add_argument('date', type=str, help='Date of the operation')
    add_parser.add_argument('op_type', type=str, help='Type of the operation')
    add_parser.add_argument('category', type=str, help='Category of the operation')
    add_parser.add_argument('value', type=float, help='Value of the operation')

    # add category
    add_cat_parser = subparsers.add_parser('add_cat', help='Add a new category to the database')
    add_cat_parser.add_argument('name_cat', type=str, help='Name of the category')
    add_cat_parser.add_argument('description_cat', type=str, help='Description of the category')

    # Analyze command
    analyze_parser = subparsers.add_parser('analyze', help='Analyze the current database status')

    # Visualize command
    visualize_parser = subparsers.add_parser('visualize', help='Visualize the current database status')

    args = parser.parse_args()

    session = setup_connection_db()

    if args.command == 'add_op':
        with session() as session:
            category = session.query(Categories).filter(Categories.name == args.category).first()
            new_expense = FinOpModel(FinOp(args.name, args.date, args.op_type, category, args.value))
            session.add(new_expense)
            session.commit()
            session.close()
    elif args.command == 'add_cat':
        with session() as session:
            new_category = Categories(name=args.name_cat, description=args.description_cat)
            session.add(new_category)
            session.commit()
            session.close()
        # Add your analysis code here
        pass
    elif args.command == 'visualize':
        # Add your visualization code here
        pass


if __name__ == "__main__":
    main()