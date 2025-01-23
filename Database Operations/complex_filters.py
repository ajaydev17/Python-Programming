"""
: SQLAlchemy allows you to create complex filters by combining conditions using
and_, or_, and other operators. These operators can be imported from sqlalchemy and used
within the filter method to specify multiple conditions in a query.
"""

from sqlalchemy import and_, or_

# Complex filter example
session = Session()
results = session.query(Student).filter(
    and_(
        Student.age >= 20,
        or_(Student.name == 'Alice', Student.name == 'Bob')
    )
).all()

for student in results:
    print(student.name)

session.close()