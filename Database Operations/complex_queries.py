"""
SQLAlchemy supports complex queries using join, filter, and aggregate
functions. You can chain these methods to create queries that involve multiple tables and
complex filtering.
"""

from sqlalchemy import func

# Complex query to find the average age of students
session = Session()
average_age = session.query(func.avg(Student.age)).scalar()
print(f"Average age: {average_age}")

# Querying with join and filter
result = session.query(Student).join(Enrollment).filter(Student.name == 'Alice').all()

for student in result:
    print(student.name)

session.close()