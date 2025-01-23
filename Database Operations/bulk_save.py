"""
Bulk inserts in SQLAlchemy can be performed using bulk_save_objects or
bulk_insert_mappings. These methods are more efficient for inserting large datasets, as
they reduce the overhead associated with ORM and commit in bulk.
"""

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

# Performing a bulk insert
students = [Student(name='Alice'), Student(name='Bob'), Student(name='Carol')]
session.bulk_save_objects(students)
session.commit()