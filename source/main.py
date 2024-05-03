"""
original author: Dominik Cedro
created: 2024-04-17
license: GSB 3.0
description: This module encapsulates main app functionalities
"""
import argparse
from .database_module.database import setup_connection_db, query_all_prepare_with_analysis
from .database_module.model.finop_model import FinOpModel
from .operations_module.financial_operation import FinOp
from .analysis_module.analysis import Analysis
from .visualization_module.visualization import Visualization
from .database_module.model.categories import Categories
import logging
import logging.config
from sqlalchemy import text


def main():

    parser = argparse.ArgumentParser(description="Python Finance App")
    subparsers = parser.add_subparsers(dest="command")

    # test database connection
    test_parser = subparsers.add_parser('test_db_connection', help='testing if connection to database is correct')

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
    analyze_parser = subparsers.add_parser('analyze_all',
                                           help='Analyze all financial operations, provides total sum and average for incomes and expenses')



    # Analyze average total by category
    analyze_cat_parser = subparsers.add_parser('analyze_by_category', help='Analyze by cateogry all expenses and incomes')
    analyze_cat_parser.add_argument('analyze_category', type=str, help='blabla')

    # Visualize command
    # visualize_parser = subparsers.add_parser('visualize', help='Visualize the current database status')
    # visualize_parser.add_argument('visualize_month', type=str, help='month to visualize data')

    # Visualize total month
    visualize_totparser = subparsers.add_parser('visualize_total_month', help='Visualize both incomes and expenses for given month')
    visualize_totparser.add_argument('visualize_total_month',type=str,help='Which month should be visualized')

    # List operations
    list_parser = subparsers.add_parser('list_operations', help='List all operations')
    list_parser.add_argument('--order', type=str, default='date', choices=['date', 'category', 'value'],
                             help='Order in which to list the operations')
    list_parser.add_argument('--direction', type=str, default='ASC', choices=['ASC', 'DESC'],
                               help='ascending or descending')
    list_parser.add_argument('--limit', type=int, default=5)

    # List categories
    category_list_parser = subparsers.add_parser('list_categories', help='List all operations')
    category_list_parser.add_argument('--limit', type=int, default=5)

    args = parser.parse_args()

    session = setup_connection_db()

    if args.command == 'list_operations':
        with session() as session:
            if args.order == 'date':
                operations = session.query(FinOpModel).order_by(FinOpModel.date).limit(args.limit).all()
            elif args.order == 'category':
                operations = session.query(FinOpModel).order_by(FinOpModel.category).limit(args.limit).all()
            elif args.order == 'value':
                operations = session.query(FinOpModel).order_by(FinOpModel.value).limit(args.limit).all()
            print(f'List operations')
            print(f'order: {args.order}, limit: {args.limit}, direction: {args.direction}')
            print('')
            for operation in operations:
                print(operation)
            print('')
            session.commit()
            session.close()

    elif args.command == 'list_categories':
        with session() as session:
            categories = session.query(Categories).limit(args.limit).all()
            print('List categories')
            print(f'limit: {args.limit}')
            print('')
            for category in categories:
                print(category)
            print('')
            session.commit()
            session.close()

    elif args.command == 'add_op':
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

    elif args.command == 'analyze_all':
        with session() as session:
            analysis = query_all_prepare_with_analysis(session)
            print('Total analysis')
            print('')
            print(f'total of all expenses: {analysis.total_expenses()}')
            print(f'average of all expenses: {analysis.average_expense()}')
            print(f'total of all incomes: {analysis.total_income()}')
            print(f'average of all incomes: {analysis.average_income()}')
            print('')
            session.commit()
            session.close()

    elif args.command == 'analyze_by_category':
        with session() as session:
            analysis = query_all_prepare_with_analysis(session)
            chosen_category = args.analyze_category
            print(f'total of all expenses for category {chosen_category}: {analysis.total_expense_category(chosen_category)}')
            print(f'average of all expenses {chosen_category}: {analysis.average_expense_category(chosen_category)}')
            print(f'total of all incomes {chosen_category}: {analysis.total_income_category(chosen_category)}')
            print(f'average of all incomes {chosen_category}: {analysis.average_income_category(chosen_category)}')
            print('')
            session.commit()
            session.close()

    # elif args.command == 'visualize':
    #     with session() as session:
    #         expenses = session.query(FinOpModel).filter(FinOpModel.op_type == 'expense')
    #         incomes = session.query(FinOpModel).filter(FinOpModel.op_type == 'income')
    #         exp_list = expenses.all()
    #         inc_list = incomes.all()
    #         analysis = Analysis(exp_list, inc_list)
    #         chosen_month = args.visualize_month
    #         Visualization(analysis).plot_total_expenses_month(chosen_month)
    #         session.commit()
    #         session.close()

    elif args.command == 'visualize_total_month':
        with session() as session:
            # TODO code below should be put in some kind of function to simplify this file, its a copy paste pattern
            # expenses = session.query(FinOpModel).filter(FinOpModel.op_type == 'expense')
            # incomes = session.query(FinOpModel).filter(FinOpModel.op_type == 'income')
            # exp_list = [expense.to_finop() for expense in expenses.all()]
            # inc_list = [income.to_finop() for income in incomes.all()]
            # analysis = Analysis(exp_list, inc_list)
            analysis=query_all_prepare_with_analysis(session)
            chosen_month = args.visualize_total_month
            Visualization(analysis).plot_total_expenses_and_incomes_month(chosen_month)


    elif args.command == 'test_db_connection':
        logger.info('test_db_connection: starting test session..')
        try:
            with session() as session:
                session.execute(text("SELECT 1"))  # simple query to test the connection
                session.commit()
                session.close()
                logger.info('test_db_connection: successful')
        except Exception as e:
            logger.error(f'test_db_connection: failed, error: {str(e)}')

if __name__ == "__main__":
    import logging

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # create a file handler
    file_handler = logging.FileHandler('example.log')
    file_handler.setLevel(logging.INFO)

    # create a stream handler
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)

    # create a logging format
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    main()