"""
Django follows an MVC (Model-View-Controller) pattern, often described as MTV
(Model-Template-View) in Django terminology. This architecture separates the application
logic, presentation, and data handling, allowing for more organized and maintainable code.
    1. Model: Defines the data structure and represents the database schema. Models are
    Python classes mapped to database tables.
    2. View: Contains the business logic, acting as a bridge between the model and
    template. Views process requests, retrieve data from models, and pass it to templates.
    3. Template: Responsible for rendering HTML and presenting data to the user.
"""

# in models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)


# in views.py
from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


# in book_list.html
"""
<!DOCTYPE html>
<html>
<body>
    <h1>Book List</h1>
    {% for book in books %}
        <p>{{ book.title }} by {{ book.author }}</p>
    {% endfor %}
</body>
</html>
"""