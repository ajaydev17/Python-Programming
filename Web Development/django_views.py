"""
Django views are functions or classes that handle HTTP requests and return HTTP
responses. Views act as the bridge between the model (data) and the template
(presentation). In Django, views contain the logic for processing requests, retrieving data
from models, applying any necessary logic, and rendering templates to present data to the
user.
There are two main types of views in Django: function-based views (FBVs) and class-based
views (CBVs). FBVs are simple functions, while CBVs are classes that offer greater flexibility
and reusability
"""

# Example of a Django view
from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})