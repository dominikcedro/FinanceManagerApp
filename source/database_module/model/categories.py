"""
original author: Dominik Cedro
created: 2024-04-02
license: BSD 3.0
description: This module contains class categories for python finance app.
"""
from sqlalchemy import Column, Integer, String
from source.database_module.model.base import Base


class Categories(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    description = Column(String(100))

    def __str__(self):
        return f'{self.name} - {self.description}'

