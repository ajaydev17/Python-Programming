"""
ORM (Object-Relational Mapping) frameworks allow developers to interact with
databases using Python objects instead of raw SQL. By using an ORM, Python classes are
mapped to database tables, and CRUD operations can be performed without writing SQL
queries directly. Popular ORM libraries include SQLAlchemy and Django ORM.
"""

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Setting up ORM
engine = create_engine('sqlite:///example.db')
Base = declarative_base()

class Student(Base):
     __tablename__ = 'students'
     id = Column(Integer, primary_key=True)
     name = Column(String)
     age = Column(Integer)

Base.metadata.create_all(engine)