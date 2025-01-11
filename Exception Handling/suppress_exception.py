"""
Python’s contextlib module has a suppress function that allows you to ignore
specific exceptions within a with block. By passing an exception type to suppress, you can
prevent interruptions due to anticipated exceptions without needing a try-except
structure. This is useful for cases where an error is expected and non-critical, so it can be
safely ignored to allow the program to continue.
"""

from contextlib import suppress

with suppress(FileNotFoundError):
    with open('non_existent_file.txt') as file:
        content = file.read() # Suppressed if the file does not exist
