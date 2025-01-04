"""
In Python, you can create custom exceptions by subclassing the built-in Exception class.
This allows you to raise specific error types that can be caught and handled by the caller,
making error handling more precise.
"""

class InvalidInputException(Exception):
    pass

def process_input(value):
    if not isinstance(value, int):
        raise InvalidInputException("Input must be an integer")
    return value ** 2

try:
    result = process_input(5)
    print(result)
except InvalidInputException as e:
    print(e)