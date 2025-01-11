"""
sys.exc_info() provides access to details about the most recent exception,
returning a tuple with the exception type, value, and traceback. This is especially useful when
you want to pass detailed exception information to other parts of the code, such as logging
functions, without using the except block directly.
"""

import sys

try:
    # This code might raise a ValueError if the input is not a number
    result = 10 / 0
except ZeroDivisionError:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print(f"An error occurred: {exc_value}")
    print("Original exception type:", exc_type.__name__)