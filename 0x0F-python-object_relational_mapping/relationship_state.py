#!/usr/bin/python3
"""
Defines the State Model and imports and sets the Base Model
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """Defines the `states` table as well as its attributes
    """
    __tablename__ = 'states'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', order_by='City.id',
                          back_populates='state')
