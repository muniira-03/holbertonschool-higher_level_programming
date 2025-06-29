#!/usr/bin/python3
"""
This script defines a SQLAlchemy ORM model for the 'states' table.
It maps the `State` class to the 'states' table, allowing easy database
interactions using Python objects.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    The State class, which represents the 'states' table of the database.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
