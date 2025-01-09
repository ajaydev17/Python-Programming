"""
In Python, you can create a custom context manager by defining a class with
__enter__ and __exit__ methods or by using the contextlib module’s @contextmanager
decorator. Context managers simplify resource management and exception handling,
automatically handling setup and cleanup tasks, which reduces the risk of resource leaks. If
an exception occurs within the with block, __exit__ will execute, ensuring resources are
properly released.
"""

from contextlib import contextmanager

@contextmanager
def open_file(file_name):
    file = None
    try:
        file = open(file_name, 'r')
        yield file
    finally:
        if file:
            file.close()

with open_file('example.txt') as f:
    print(f.read())

