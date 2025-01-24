"""
SQLAlchemy handles transactions using a session object. By default, any operation
within a session is part of a transaction, and you can use commit() to save changes or
rollback() to revert them in case of an error.
"""

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

# Adding a new student
new_student = Student(name='Alice', age=20)

session.add(new_student)
session.commit() # Commits the transaction to save data
session.close()