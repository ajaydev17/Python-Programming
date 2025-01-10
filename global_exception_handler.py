"""
A global exception handler can be set by assigning a custom function to
sys.excepthook. This function will handle all unhandled exceptions in the program. It’s
commonly used for logging purposes in applications, allowing all unhandled exceptions to
be logged uniformly without terminating the program abruptly.
"""

import sys

def global_exception_handler(exc_type, exc_value, exc_traceback):
    print("Unhandled exception: ", exc_value)

sys.excepthook = global_exception_handler

# Now, any unhandled exception in the program will be caught by the global exception handler
raise ValueError("Unhandled exception") # This will be caught by the global exception handler