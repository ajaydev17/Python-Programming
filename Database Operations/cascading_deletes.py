"""
Cascading deletes in SQLAlchemy allow related records to be automatically deleted
when a parent record is deleted. This is achieved by setting the cascade argument in the
relationship() function, typically with the delete, delete-orphan options.
"""

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///example.db')
Base = declarative_base()

class Student(Base):
     __tablename__ = 'students'
     id = Column(Integer, primary_key=True)
     name = Column(String)
     enrollments = relationship("Enrollment", cascade="all, delete-orphan")


class Enrollment(Base):
    __tablename__ = 'enrollments'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))

Base.metadata.create_all(engine)