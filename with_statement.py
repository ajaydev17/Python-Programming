# The with statement in Python is used to wrap the execution of a block of code with methods
# defined by a context manager. It's often used when working with file operations, database connections,
# or network requests to ensure that the resources are properly managed, even if an error occurs.


# Example 1: Using a file with the 'with' statement
with open('example.txt', 'r') as file:
    content = file.read()