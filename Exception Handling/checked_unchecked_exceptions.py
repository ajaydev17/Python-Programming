"""
Checked exceptions are exceptions that must be either handled or declared in the
method signature, as seen in languages like Java. Unchecked exceptions, however, do not
require explicit handling. Python does not have checked exceptions; all exceptions are
unchecked. This means that in Python, developers are not forced to handle exceptions,
providing flexibility but also requiring careful error management to prevent program crashes.
"""

def divide(a, b):
    return a / b

try:
    result = divide(10, 0)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")