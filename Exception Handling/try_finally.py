"""
When an exception is raised in both try and finally blocks, the exception from the
finally block takes precedence and effectively overrides the exception from the try block.
This can cause the original exception in try to be lost, making it harder to debug. To capture
both exceptions, you can store the exception from try before the finally block, allowing
you to review it if needed.
"""

try:
    try:
        result = 1 / 0 # ZeroDurationException
    finally:
        raise ValueError("Exception in finally block")
except Exception as e:
    original_exception = e
    print("Original exception:", original_exception)