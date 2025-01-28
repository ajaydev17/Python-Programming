"""
Asynchronous views in Django allow for non-blocking request handling by using
Python’s async and await keywords. Django introduced support for async views in version
3.1, enabling views to handle I/O-bound tasks (e.g., network requests, database queries)
without blocking other requests.

Async views are beneficial when working with asynchronous databases, APIs, or other
external resources where waiting times can be significant.
"""

# in views.py
from django.http import JsonResponse
import asyncio

async def my_async_view(request):
    # simulate an I/O-bound task
    await asyncio.sleep(1)
    return JsonResponse({'data': 'Hello, World!'})