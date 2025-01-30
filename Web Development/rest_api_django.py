"""
To create a REST API in Django, developers typically use Django REST Framework
(DRF), which provides tools for building APIs with serializers, views, and routers. DRF allows
for easily defining API endpoints, handling requests, serializing data, and managing
authentication.

A REST API in Django consists of views for handling HTTP methods (GET, POST, PUT, DELETE)
and serializers to convert complex data types into JSON.
"""

# in serializers.py
from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author']


# in views.py
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# in urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]