"""
Exception chaining in Python occurs when an exception is raised while handling
another exception, linking the two exceptions together. Python supports implicit chaining,
where an exception raised inside an except block automatically links to the original
exception, and explicit chaining, where you use the raise ... from ... syntax to specify
the direct cause. Exception chaining is useful for debugging, as it provides a complete error
context, allowing developers to trace back through multiple levels of exceptions.
"""

try:
    # This code might raise a ValueError if the input is not a number
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        raise ValueError("Cannot divide by zero") from e
except ValueError as ve:
    print("Error:", ve)
    print("Original exception: ", ve.__cause__)
