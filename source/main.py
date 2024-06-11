"""
original author: Dominik Cedro
created: 2024-04-17
license: GSB 3.0
description: This module encapsulates main app functionalities
"""

import argparse
from .database.database import setup_connection_db, query_all_prepare_with_analysis, query_by_month, query_by_category
from .database.model.finop_model import FinOpModel
from .operations.financial_operation import FinOp
from .analysis.analysis import Analysis
from .visualization.visualization import Visualization
from .database.model.categories import Categories
from sqlalchemy import text
import logging.config
from .common.logging_config import LOGGING_CONFIG
from sqlalchemy import func


# setup logging using LOGGING_CONFIG dictonary in common dir
logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)


def main():

    parser = argparse.ArgumentParser(description="Python Finance App")
    subparsers = parser.add_subparsers(dest="command")

    # test database connection
    test_parser = subparsers.add_parser('test_db_connection', help='Testing if connection to database is correct.')

    # Add financial operation command
    add_parser = subparsers.add_parser('add_op', help='Add a new financial operation to the database.')
    add_parser.add_argument('name_op', type=str, help='Name of the operation.')
    add_parser.add_argument('date', type=str, help='Date of the operation in format: YYYY-MM-DD HH:mm:ss')
    add_parser.add_argument('op_type', type=str, help='Type of the operation: "expense"/"income"')
    add_parser.add_argument('category', type=str, help='Category of the operation, chose a valid category.')
    add_parser.add_argument('value', type=float, help='Value of the operation, float number.')

    # add category
    add_cat_parser = subparsers.add_parser('add_cat', help='Add a new category to the database.')
    add_cat_parser.add_argument('name_cat', type=str, help='Name of the category.')
    add_cat_parser.add_argument('description_cat', type=str, help='Description of the category.')


    # Analyze average total (avgtot) command
    analyze_parser = subparsers.add_parser('analyze_all', help='Analyze all financial operations, '
                                                               'provides total sum and average for all rows,'
                                                               'default limit is 1 000 operations.')


    # Analyze by category
    analyze_cat_parser = subparsers.add_parser('analyze_by_category', help='Analyze all operations '
                                                                           'by given category,'
                                                                           'chose valid category!')
    analyze_cat_parser.add_argument('analyze_category', type=str, help='Category criterion,'
                                                                       ' must be a valid one!')


    # Visualize total month
    visualize_totparser = subparsers.add_parser('visualize_total_month', help='Visualize both incomes and expenses'
                                                                              ' for given month')
    visualize_totparser.add_argument('visualize_total_month', type=str, help='Name of the month criterion.')


    # List operations
    list_parser = subparsers.add_parser('list_operations', help='List all operations, sorted by date ascending,'
                                                                ' limit: 5 by default.')
    list_parser.add_argument('--order', type=str, default='date', choices=['date', 'category', 'value'],
                             help='Order in which to list the operations: "date"/"category"/"value".'
                                  ' Default value : "date"')
    list_parser.add_argument('--direction', type=str, default='ASC', choices=['ASC', 'DESC'],
                               help='Direction of sorting the operations: "ASC"/"DESC"')
    list_parser.add_argument('--limit', type=int, default=5, help='Limit of operations to be shown,'
                                                                  ' Default value: 5')

    # List categories
    category_list_parser = subparsers.add_parser('list_categories', help='List all operations, default limit is 5')
    category_list_parser.add_argument('--limit', type=int, default=5, help='Limit of operations to be shown,'
                                                                  ' Default value: 5')

    args = parser.parse_args()
    session = setup_connection_db()
    if session is None:
        exit(1)

    if args.command == 'list_operations':
        with session() as session:
            logger.info('List operations argsparser command running')
            operations = session.query(FinOpModel).all()
            if not operations:
                logger.info("No operations")
                exit(1)
            if args.order == 'date':
                if args.direction == 'ASC':
                    operations = session.query(FinOpModel).order_by(FinOpModel.date.asc()).limit(args.limit).all()
                else:
                    operations = session.query(FinOpModel).order_by(FinOpModel.date.desc()).limit(args.limit).all()
            elif args.order == 'category':
                if args.direction == 'ASC':
                    operations = session.query(FinOpModel).order_by(FinOpModel.category.asc()).limit(args.limit).all()
                else:
                    operations = session.query(FinOpModel).order_by(FinOpModel.category.desc()).limit(args.limit).all()
            elif args.order == 'value':
                if args.direction == 'ASC':
                    operations = session.query(FinOpModel).order_by(FinOpModel.value.asc()).limit(args.limit).all()
                else:
                    operations = session.query(FinOpModel).order_by(FinOpModel.value.desc()).limit(args.limit).all()
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
            logger.info('List categories argsparser command running')
            categories = session.query(Categories).limit(args.limit).all()
            if not categories:
                logger.info('No categories')
                print("No categories")
                session.commit()
                session.close()
                exit(0)
            logger.debug(f'Returned {len(categories)} categories objects in response')
            logger.debug(f'Return limit set to {args.limit}')
            print('List categories')
            print('')
            for category in categories:
                print(category)
            print('')
            session.commit()
            session.close()

    elif args.command == 'add_op':
        with session() as session:
            logger.info('Add operation argsparser command running')
            category_lower = args.category.lower()
            category = session.query(Categories).filter(func.lower(Categories.name) == category_lower).first()
            if category is None:
                logger.error(f"Category '{args.category}' does not exist.")
                print(f"Category '{args.category}' does not exist.")
                session.commit()
                session.close()
                exit(0)
            new_operation = FinOpModel(FinOp(args.name_op, args.date, args.op_type, category, args.value))
            session.add(new_operation)

            print("Added new operation: ")
            print(f" {args.name_op} - {args.date} - {args.op_type} - {category} - {args.value}")
            session.commit()
            session.close()

    elif args.command == 'add_cat':
        with session() as session:
            name = args.name_cat
            description = args.description_cat
            category = session.query(Categories).filter(Categories.name == name.lower()).first()
            if category:
                logger.error(f"Category '{name}' already exists")
                print(f"Category '{name}' already exists")
                session.commit()
                session.close()
            new_category = Categories(name=name, description=description)
            session.add(new_category)
            print("Added new category: ")
            print(f"{args.name_cat} - {args.description_cat}")
            session.commit()
            session.close()



    elif args.command == 'analyze_all':
        with session() as session:
            analysis = query_all_prepare_with_analysis(session)
            if not analysis.expenses:
                logger.info('analyze_all: no expenses present')
                average_expense = 0
            else:
                average_expense = analysis.average_expense()

            if not analysis.incomes:
                logger.info('analyze_all: no incomes present')
                average_income = 0
            else:
                average_income = analysis.average_income()
            logger.info('Total analysis successful')
            print("Analyze_all results: ")
            print(f'Total of all expenses: {float(analysis.total_expenses())}')
            print(f'Average of all expenses: {average_expense}')
            print(f'Total of all incomes: {analysis.total_income()}')
            print(f'Average of all incomes: {average_income}')
            print('')
            session.commit()
            session.close()

    elif args.command == 'analyze_by_category':
        with session() as session:
            # check if category exists
            category = session.query(Categories).filter(Categories.name == args.analyze_category).first()
            if category is None:
                logger.error(f"Category '{args.analyze_category}' does not exist.")
                print(f"Category '{args.analyze_category}' does not exist.")
                session.commit()
                session.close()
                exit(0)
            chosen_category = category.name
            analysis = query_by_category(session, chosen_category)
            print("Analyze by category results: ")

            if not analysis.expenses:
                logger.info('analyze_all: no expenses present')
                average_expense = 0
            else:
                average_expense = analysis.average_expense_category(chosen_category)
            if not analysis.incomes:
                logger.info('analyze_all: no incomes present')
                average_income = 0
            else:
                average_income = analysis.average_income_category(chosen_category)
            # average_income = analysis.average_income_category(chosen_category)
            # average_expense = analysis.average_expense_category(chosen_category)

            print(f'total of all expenses for category {chosen_category}:'
                  f' {float(analysis.total_expense_category(chosen_category))}')
            print(f'average of all expenses {chosen_category}: {float(average_expense)}')
            print(f'total of all incomes {chosen_category}: {float(analysis.total_income_category(chosen_category))}')
            print(f'average of all incomes {chosen_category}: {float(average_income)}')
            print('')
            session.commit()
            session.close()

    elif args.command == 'visualize_total_month':
        with session() as session:
            chosen_month = args.visualize_total_month
            analysis = query_by_month(session,chosen_month)
            try:
                Visualization(analysis).plot_total_expenses_and_incomes_month(chosen_month)
            except ValueError as e:
                print('Incorrect month name')
                session.commit()
                session.close()

    elif args.command == 'test_db_connection':
        # tests the connection by starting session and executing simple SELECT 1 query, returns log if successful.
        try:
            with session() as session:
                session.execute(text("SELECT 1"))
                session.commit()
                session.close()
                logger.info('test_db_connection: successful')
                print("Connection to database successful")
        except Exception as e:
            print("Connection to database NOT successful")
            logger.error(f'test_db_connection: failed, error: {str(e)}')
            exit(0)


if __name__ == "__main__":

    main()