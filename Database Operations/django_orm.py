"""
Django ORM provides a way to define database models as Python classes. These
models are mapped to database tables, and you can perform CRUD operations using
Django’s ORM methods without writing SQL queries.
"""

from django.db import models

class Student(models.Model):
     name = models.CharField(max_length=100)
     age = models.IntegerField()