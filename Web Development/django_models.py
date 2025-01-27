"""
Django models are Python classes that define the structure of data in a Django
application. They map to database tables and define the fields and behaviors of stored data.
Each model class corresponds to a single table in the database, and each attribute in the
model class represents a column in that table.
Django provides a powerful ORM that allows developers to create, retrieve, update, and
delete records from the database using Python code, without needing to write SQL.
"""

# Example of a Django model
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.title} by {self.author}'

# usage in views.py
from .models import Book
from django.shortcuts import render

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})