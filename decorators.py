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


