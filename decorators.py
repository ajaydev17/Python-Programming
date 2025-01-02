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
