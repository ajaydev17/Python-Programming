"""
Memoization is an optimization technique where the results of expensive function calls are
cached so that future calls with the same parameters can return the result instantly. This is
particularly useful in recursive functions, like calculating Fibonacci numbers.
"""

"""
In Python, memoization can be implemented using a dictionary or the
@functools.lru_cache decorator, which caches results automatically.
"""

from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(30)) # Outputs: 832040