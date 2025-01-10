"""
To customize messages in custom exceptions, define an __init__ method that
accepts a message parameter. This allows you to provide specific error messages that explain
why the exception was raised. Custom messages make exceptions more informative and
easier to debug.
"""

class InvalidInputException(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
    # This code might raise an InvalidInputException if the input is not a number
    raise InvalidInputException("Invalid input")
except InvalidInputException as e:
    print(f"An error occurred: {e}")