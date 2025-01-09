"""
Effective exception handling in Python involves several best practices:

1. Use specific exceptions: Catch specific exceptions (like ValueError or TypeError)
instead of a generic Exception, which makes error handling more targeted and
precise.

2. Avoid suppressing exceptions: Avoid using except: pass or similar patterns, as this
suppresses all errors, including unexpected ones, which can make bugs harder to
detect.

3. Use finally for cleanup: Ensure resources are released with finally, which
guarantees cleanup actions regardless of success or failure.

4. Log exceptions: Use the logging module to record exceptions with their tracebacks,
especially in production environments, for later debugging.

5. Raise custom exceptions: Use custom exceptions for domain-specific errors, which
adds clarity and improves error handling.

6. Minimize code in try blocks: Keep only the code that may raise exceptions inside try
blocks to reduce unintended exception handling.
"""

import logging

def process_data(data):
    try:
        result = int(data) / 2
    except ValueError:
        logging.error("Invalid input, cannot convert to integer.", exc_info=True)
    except ZeroDivisionError:
        logging.error("Cannot divide by zero.", exc_info=True)
    else:
        return result
    finally:
        print("Processing data is done.")