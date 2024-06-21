#!/usr/bin/python3
"""Defines the City Model that Inherits from the Base Model
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base, State


class City(Base):
    """ Defines the `cities` table as well as its attributes and relationships
    """
    __tablename__ = 'cities'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship('State', backref='cities')
