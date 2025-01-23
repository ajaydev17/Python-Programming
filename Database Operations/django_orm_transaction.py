"""
In Django ORM, transactions are managed using the atomic decorator or context
manager. This ensures that a group of operations are completed as a single transaction,
either fully completing or rolling back on failure.
"""

from django.db import transaction

@transaction.atomic
def create_student(name, age):
     student = Student(name=name, age=age)
     student.save()