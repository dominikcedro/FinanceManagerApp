"""
original author: Dominik Cedro
created: 2024-04-03
license: GSB 3.0
description: This module contains Base class which is base class inheriting from DeclarativeBase from sqlalchemy.
"""
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base class for all database tables from sqlalchemy ORM.
    """
    pass