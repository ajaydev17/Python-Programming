"""
BaseException is the root of the exception hierarchy in Python, while Exception is a
subclass of BaseException designed for most error-handling cases. BaseException includes
all exceptions, even system-exit exceptions like SystemExit, KeyboardInterrupt, and
GeneratorExit, which are generally not intended for regular program errors. Using
Exception in except clauses ensures only program-related errors are caught, leaving
system-level exceptions to terminate the program.
"""

try:
    # This code might raise a ValueError if the input is not a number
    # some code
    pass
except Exception as e:
    print(f"An error occurred: {e}")

# This won't catch system-level exceptions like KeyboardInterrupt