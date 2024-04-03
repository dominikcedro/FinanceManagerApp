"""
original author: Dominik Cedro
created: 2024-04-02
license: GSB 3.0
description: This module contains database_module initialization script using sqlalchemy.
"""
from sqlalchemy import create_engine
from source.database_module.model.base import Base
from source.database_module.model.finop_model import FinOpModel
from source.database_module.model.categories import Categories
from sqlalchemy.orm import sessionmaker

# Replace the following fields with your actual data
username = ' '
password = ' '
host = 'localhost'
database_name = 'financedb'

engine = create_engine(f'mysql://{username}:{password}@{host}/{database_name}')

Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()


