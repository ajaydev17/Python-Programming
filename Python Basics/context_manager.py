# A context manager in python is a class or function that manages resources using the with statement
# It typically provides two methods __enter__ and __exit__.

# 1. __enter__
# This method is executed when the 'with' block is entered
# It performs setup tasks like acquiring a resource, initializing a connection or locking a file.
# The return value of this method is optionally bound to the variable after the 'as' keyword in
# the with statement

# 2. __exit__(exc_type, exc_value, traceback)
# This method is executed when the 'with' block is exited.
# It performs clean up tasks like releasing a resource, closing a connection or unlocking a resource.
# It receives three arguments
    # exc_type: Exception class (if any) that caused the with block to exit.
    # exc_value: Exception value (if any) that caused the with block to exit.
    # traceback: Traceback object (if any) that caused the with block to exit.
# If the method returns True, it suppresses the exception

# Example

class MyContextManager:
    def __enter__(self):
        print("Entering the context manager")
        return self  # Returning the instance of the context manager

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context manager")
        if exc_type:
            print(f"An exception occurred: {exc_value}")
        print("Exiting the context")
        return False  # If False, the exception is re-raised, True suppresses the exception


# Example of Database Connection Context Manager

import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        return self.connection  # Returning the database connection object

    def __exit__(self, exc_type, exc_value, traceback):
        if self.connection:
            self.connection.close()
            print("Database connection closed")

with DatabaseConnection('example.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    print(cursor.fetchall())


# creating a context manager with contextlib
# No need to define __enter__ and __exit__

from contextlib import contextmanager

@contextmanager
def my_context():
    print("Entering the context manager")
    try:
        yield "resource"
    finally:
        print("Exiting the context manager")

with my_context as context:
    print(context)

