"""
original author: Dominik Cedro
created: 2024-04-03
license: BSD 3.0
description: This module contains class FinOpModel that provides ORM based on FinOp.
"""

from source.operations_module.financial_operation import FinOp
from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from source.database_module.model.base import Base
from sqlalchemy.orm import relationship



class FinOpModel(Base):
    """
    This class represents a single financial operation, either an expense or an income mapped to ORM.
    """
    __tablename__ = 'financial_operations'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    date = Column(DateTime)
    op_type = Column(String(50))
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship("Categories", back_populates="financial_operations")

    value = Column(Float)

    def __init__(self, finop: FinOp):
        self.name = finop.name
        self.date = finop.date
        self.op_type = finop.op_type
        self.category = finop.category
        self.value = finop.value

    def __repr__(self):
        return f'{self.name} - {self.date} - {self.op_type} - {self.category} - {self.value}'