"""
original author: Dominik Cedro
created: 2024-04-02
license: GSB 3.0
description: This module contains database initialization script using sqlalchemy.
"""
import os

import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_

from .model.base import Base
from .model.finop_model import FinOpModel
from .model.categories import Categories
from ..analysis.analysis import Analysis
import logging.config
from source.common.logging_config import LOGGING_CONFIG
MAX_COUNT_ITEMS_DB: int = 1000

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger(__name__)

def setup_connection_db():

    dir_path = os.path.dirname(os.path.realpath(__file__))

    config_path = os.path.join(dir_path, 'database_config.json')

    with open(config_path) as f:
        config = json.load(f)
    username = config['username']
    password = config['password']
    host = config['host']
    database_name = config['database_name']

    engine = create_engine(f'mysql://{username}:{password}@{host}/{database_name}')

    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    return Session


def query_all_prepare_with_analysis(session) -> Analysis | None:
    """
    This function queries all rows from database and prepares them as analysis module
    :param session:
    :return:
    """
    # check if amount of items is higher than 1 000 then abort if True
    if count_entries_in_db(session, MAX_COUNT_ITEMS_DB):
        return None
    expenses = session.query(FinOpModel).filter(FinOpModel.op_type == 'expense')
    incomes = session.query(FinOpModel).filter(FinOpModel.op_type == 'income')
    exp_list = [expense.to_finop() for expense in expenses.all()]
    inc_list = [income.to_finop() for income in incomes.all()]
    analysis = Analysis(exp_list, inc_list)
    return analysis

def count_entries_in_db(session, count):
    count = session.query(FinOpModel).count()
    if count > 1000:
        logger.warning(f"Count of items in db over {count}")
        return True
    return False


if __name__ == "__main__":
    pass