"""
SQLAlchemy handles table relationships by using relationship() and
ForeignKey() in its ORM layer. Relationships such as one-to-many or many-to-many can be
defined within class models, enabling easy navigation between related data objects in
Python code.
"""

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

engine = create_engine('sqlite:///example.db')
Base = declarative_base()

class Student(Base):
     __tablename__ = 'students'
     id = Column(Integer, primary_key=True)
     name = Column(String)


class Enrollment(Base):
     __tablename__ = 'enrollments'
     id = Column(Integer, primary_key=True)
     student_id = Column(Integer, ForeignKey('students.id'))
     student = relationship('Student', back_populates="enrollments")

Student.enrollments = relationship('Enrollment', order_by=Enrollment.id, back_populates="student")
Base.metadata.create_all(engine)