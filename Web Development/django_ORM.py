"""
Django’s ORM (Object-Relational Mapping) allows developers to interact with the
database using Python code rather than raw SQL queries. The ORM abstracts the database
layer, allowing developers to perform CRUD (Create, Read, Update, Delete) operations on
models, which are Python classes mapped to database tables.

With the ORM, Django automatically generates SQL statements based on the model
definitions, making it easier to manage data and perform complex queries without writing
SQL directly.
"""

# Example of a Django model
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.title} by {self.author}'


# using ORM to create and retrieve records
from .models import Book

# Create a new book record
book = Book(title="Python Programming", author="Guido van Rossum")
book.save()

# Retrieve all book records
books = Book.objects.all()