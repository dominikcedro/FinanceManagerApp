# database.py
from sqlalchemy import create_engine, Table
import MySQLdb
from sqlalchemy.orm import sessionmaker
from financial_operations import Expense, Income
from categories import Categories  # Import the Categories class
from base import Base

engine = create_engine('url') ## zmienna środowiskowa??

Base.metadata.create_all(engine)