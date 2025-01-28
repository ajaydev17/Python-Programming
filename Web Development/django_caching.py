"""
Caching in Django is a technique to store the results of expensive operations,
reducing the need to recompute them. Django provides various caching methods, including
database, file-based, memory-based, and caching with external systems like Redis or
Memcached.

Common methods:
    1. Per-View Caching: Caches the output of entire views.
    2. Template Fragment Caching: Caches parts of templates.
    3. Low-Level Caching API: Allows custom caching of specific data.
"""

# in views.py
from django.views.decorators.cache import cache_page
from django.shortcuts import render

@cache_page(60 * 15)  # cache for 15 minutes
def my_view(request):
    # expensive operation
    context = {'data': 'Hello, World!'}
    return render(request, 'my_template.html', context)