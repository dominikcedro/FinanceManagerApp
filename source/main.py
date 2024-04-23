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

    # Analyze average total (avgtot) command
    analyze_parser = subparsers.add_parser('analyze_avgtot', help='Analyze the current database status')
    # analyze_parser.add_argument('month to analyze', type=str,help='month that will be analyzed')
    # analyze_parser.add_argument('analyze_operation', type=str, help='what kind of analysis to perform')
    # analyze_parser.add_argument('analyze_type', type=str, help='nobody reads that')


    # Analyze average total by category
    analyze_cat_parser = subparsers.add_parser('analyze_by_category', help='Analyze by cateogry all expenses and incomes')
    analyze_cat_parser.add_argument('analyze_category', type=str, help='blabla')

    # Visualize command
    visualize_parser = subparsers.add_parser('visualize', help='Visualize the current database status')
    visualize_parser.add_argument('visualize_month', type=str, help='month to visualize data')

    args = parser.parse_args()

    session = setup_connection_db()

    if args.command == 'add_op':
        with session() as session:
            category = session.query(Categories).filter(Categories.name == args.category).first()
            new_operation = FinOpModel(FinOp(args.name_op, args.date, args.op_type, category, args.value))
            session.add(new_operation)
            session.commit()
            session.close()
    elif args.command == 'add_cat':
        with session() as session:
            new_category = Categories(name=args.name_cat, description=args.description_cat)
            session.add(new_category)
            session.commit()
            session.close()

    elif args.command == 'analyze_avgtot':
        with session() as session:
            expenses = session.query(FinOpModel).filter(FinOpModel.op_type == 'expense')
            incomes = session.query(FinOpModel).filter(FinOpModel.op_type == 'income')
            exp_list = expenses.all()
            inc_list = incomes.all()
            analysis = Analysis(exp_list, inc_list)
            print(f'total of all expenses {analysis.total_expenses()}')
            print(f'average of all expenses {analysis.average_expense()}')
            print(f'total of all incomes {analysis.total_income()}')
            print(f'average of all incomes {analysis.average_income()}')
            session.commit()
            session.close()

    elif args.command == 'analyze_by_category':
        with session() as session:
            expenses = session.query(FinOpModel).filter(FinOpModel.op_type == 'expense')
            incomes = session.query(FinOpModel).filter(FinOpModel.op_type == 'income')
            exp_list = expenses.all()
            inc_list = incomes.all()
            analysis = Analysis(exp_list, inc_list)
            chosen_category = args.analyze_category
            print(f'total of all expenses for category {chosen_category} : {analysis.total_expense_category(chosen_category)}')
            print(f'average of all expenses {chosen_category} :{analysis.average_expense_category(chosen_category)}')
            print(f'total of all incomes {chosen_category} :{analysis.total_income_category(chosen_category)}')
            print(f'average of all incomes {chosen_category} :{analysis.average_income_category(chosen_category)}')
            session.commit()
            session.close()

    elif args.command == 'visualize':
        with session() as session:
            expenses = session.query(FinOpModel).filter(FinOpModel.op_type == 'expense')
            incomes = session.query(FinOpModel).filter(FinOpModel.op_type == 'income')
            exp_list = expenses.all()
            inc_list = incomes.all()
            analysis = Analysis(exp_list, inc_list)
            chosen_month = args.visualize_month
            Visualization(analysis).plot_total_expenses_month(chosen_month)

            session.commit()
            session.close()

if __name__ == "__main__":
    main()