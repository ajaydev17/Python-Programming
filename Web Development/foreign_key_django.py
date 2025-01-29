"""
: In Django, a ForeignKey is a field type that defines a one-to-many relationship
between models. It is used when each record in one table can relate to multiple records in
another table, while each record in the second table relates back to a single record in the
first.

ForeignKey fields are defined in a model with a reference to another model class, and
Django manages database-level foreign key constraints.
"""

from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} by {self.author}'


# Example of creating and querying related records
author = Author.objects.create(name="John Doe")
book1 = Book.objects.create(title="Book 1", author=author)

# Query all books by a specific author
books_by_author = Book.objects.filter(author=author)

# Query the author of a specific book
book_author = book1.author