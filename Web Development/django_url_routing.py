"""
In Django, URL routing is managed by defining URL patterns in the urls.py file. URL
patterns are created using Django’s path or re_path functions, and they map specific URL
paths to corresponding view functions or class-based views. This allows Django to handle
different URL endpoints and invoke the appropriate view for each request.
URL patterns are defined using regular expressions or path converters, and they can capture
variables from URLs to pass as arguments to views.
"""

# in urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:book_id>/', views.book_detail, name='book_detail'),
]

# in views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def book_detail(request, book_id):
    return render(request, 'book_detail.html', {'book_id': book_id})