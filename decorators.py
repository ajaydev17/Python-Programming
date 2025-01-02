# Decorators are powerful tool for modifying or extending the behavior of functions or classes
# They work by taking a function as input, adding some additional functionality, and returning
# a new function with enhanced capabilities.


# Simple decorator example
def decorator_function(func):
    def wrapper_function():
        print("Before function execution")
        func()
        print("After function execution")
    return wrapper_function

@decorator_function
def my_function():
    print("Inside my_function")


# logging function calls with decorators

def log_function_calls(func):
    import functools

    # This below line preserves the metadata like function name and docstring etc
    @functools.wraps(func)
    def wrapper_function(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned {result}")
        return result
    return wrapper_function


@log_function_calls
def add_numbers(a, b):
    return a + b


# logging to file using logging module

import logging

# configure the logger
logging.basicConfig(level=logging.INFO, filename='function_calls.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def log_func_calls(func):
    import functools

    # This below line preserves the metadata like function name and docstring etc
    @functools.wraps(func)
    def wrapper_function(*args, **kwargs):
        logging.info(f"Calling function '{func.__name__}' with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        logging.info(f"Function '{func.__name__}' returned {result}")
        return result
    return wrapper_function


@log_func_calls
def add_numbers(a, b):
    return a + b


# decorator for classes

def log_methods(cls):
    import functools

    def decorator(func):
        @functools.wraps(func)
        def wrapper_function(*args, **kwargs):
            print(f"Calling method '{func.__name__}' of class '{cls.__name__}' with arguments {args} and keyword arguments {kwargs}")
            result = func(*args, **kwargs)
            print(f"Method '{func.__name__}' of class '{cls.__name__}' returned {result}")
            return result
        return wrapper_function

    # cls.__dict__ is a direct reference to the __dict__ attribute of the class. It stores the namespace of the class as a dictionary.
    # It provides the same information as vars(cls) in most cases.
    # cls.__dict__ will raise an AttributeError if __dict__ doesn’t exist.
    for attr in cls.__dict__:
        if callable(getattr(cls, attr)):
            setattr(cls, attr, decorator(getattr(cls, attr)))

    return cls


@log_methods
class Example:
    def method_a(self, x):
        return x + 10

    def method_b(self, y):
        return y * 2

# Test the class
obj = Example()
print(obj.method_a(5))  # Output: method_a works correctly.
print(obj.method_b(3))  # Output: method_b works correctly.

# another way of doing it

def log_methods(cls):
    import functools

    # vars() is a built-in Python function that returns the __dict__ attribute of the given object (if it exists).
    # It provides a dictionary of the object's attributes (name-value pairs).
    # If the object doesn’t have a __dict__ attribute, vars() raises a TypeError.
    for attr_name, attr_value in vars(cls).items():
        if callable(attr_value):  # Check if the attribute is a method
            def make_wrapper(method):
                @functools.wraps(method)
                def wrapper(*args, **kwargs):
                    print(f"Calling method '{method.__name__}' with arguments {args} and {kwargs}")
                    result = method(*args, **kwargs)
                    print(f"'{method.__name__}' returned {result}")
                    return result

                return wrapper

            # Wrap the method with the correct function
            setattr(cls, attr_name, make_wrapper(attr_value))
    return cls


@log_methods
class Example:
    def method_a(self, x):
        return x + 10

    def method_b(self, y):
        return y * 2


# Test the class
obj = Example()
print(obj.method_a(5))  # Output: method_a works correctly.
print(obj.method_b(3))  # Output: method_b works correctly.


# Authentication Decorator in Flask

from flask import Flask, request, jsonify

app = Flask(__name__)

def require_token(func):
    import functools
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')  # Extract token from headers
        if not token or token != "my-secret-token":
            return jsonify({"error": "Unauthorized"}), 401
        return func(*args, **kwargs)
    return wrapper

@app.route('/protected')
@require_token
def protected():
    return jsonify({"message": "Welcome to the protected resource!"})

if __name__ == '__main__':
    app.run(debug=True)

# Authentication Decorator with Django

from django.http import JsonResponse

def require_authentication(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_authenticated:  # Django's built-in user authentication
            return JsonResponse({"error": "Unauthorized"}, status=401)
        return func(request, *args, **kwargs)
    return wrapper

# Usage example
from django.shortcuts import render

@require_authentication
def protected_view(request):
    return JsonResponse({"message": "Welcome to the protected view!"})


# Basic Access Control Decorator

def access_control(permission_check):
    """
    A decorator to enforce access control.
    """
    import functools
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if not permission_check():
                return "Access Denied: You don't have permission to perform this action.", 403
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Example Permission Check Function
def is_admin():
    # Replace with actual logic to check user role
    return True  # Simulate admin user

# Apply Access Control
@access_control(is_admin)
def admin_action():
    return "Admin action performed!"

# Test
print(admin_action())  # Output: "Admin action performed!"

# Basic Resource Management Example

def manage_resource(acquire, release):
    """
    A decorator to manage resources.
    """
    import functools
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            resource = acquire()  # Acquire the resource
            try:
                return func(resource, *args, **kwargs)  # Pass the resource to the function
            finally:
                release(resource)  # Release the resource
        return wrapper
    return decorator

# Example: File Resource Management
def open_file():
    print("Opening file...")
    return open("example.txt", "w")

def close_file(file):
    print("Closing file...")
    file.close()

@manage_resource(open_file, close_file)
def write_to_file(file, content):
    print("Writing to file...")
    file.write(content)

# Usage
write_to_file("Hello, world!")
# Output:
# Opening file...
# Writing to file...
# Closing file...


# Context Managers with Decorators

from contextlib import contextmanager

def manage_resource_with_context(context_manager):
    """
    A decorator to manage resources using a context manager.
    """
    import functools
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with context_manager() as resource:
                return func(resource, *args, **kwargs)
        return wrapper
    return decorator

# Example: Database Connection
@contextmanager
def db_connection():
    print("Connecting to database...")
    conn = "DatabaseConnection"  # Simulate a database connection
    yield conn
    print("Closing database connection...")

@manage_resource_with_context(db_connection)
def query_database(conn, query):
    print(f"Executing query: {query} on {conn}")

# Usage
query_database("SELECT * FROM users")
# Output:
# Connecting to database...
# Executing query: SELECT * FROM users on DatabaseConnection
# Closing database connection...


# Managing External API Rate Limits

import time

def rate_limit(max_calls, time_period):
    """
    A decorator to limit the rate of function calls.
    """
    from collections import deque
    import functools

    calls = deque()

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_time = time.time()
            while calls and calls[0] < current_time - time_period:
                calls.popleft()
            if len(calls) >= max_calls:
                raise Exception("Rate limit exceeded!")
            calls.append(current_time)
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Example: API Call
@rate_limit(max_calls=3, time_period=10)  # Max 3 calls per 10 seconds
def api_call(endpoint):
    print(f"Calling API endpoint: {endpoint}")

# Usage
for i in range(5):
    try:
        api_call(f"/endpoint/{i}")
    except Exception as e:
        print(e)
# Output:
# Calling API endpoint: /endpoint/0
# Calling API endpoint: /endpoint/1
# Calling API endpoint: /endpoint/2
# Rate limit exceeded!
# Rate limit exceeded!






