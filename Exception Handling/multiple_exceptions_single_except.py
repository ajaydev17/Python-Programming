"""
You can handle multiple exceptions in a single except block by passing a tuple of
exceptions. This allows you to apply the same handling logic for different types of exceptions,
making the code more concise and readable. It’s particularly useful when similar actions (like
logging or retrying) are appropriate for multiple exceptions.
"""

try:
    # This code might raise a ValueError or TypeError if the input is not a number
    result = 10 / 0
except (ValueError, TypeError):
    print("Error: Invalid input. Please provide a valid number.")