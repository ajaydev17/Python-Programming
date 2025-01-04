"""
In Python 2, dividing two integers results in integer (or floor) division by default. For
example, 5 / 2 would yield 2, discarding the decimal portion. This behavior can lead to
unexpected results if floating-point division is expected. In Python 3, however, dividing two
integers defaults to true division, returning a float (e.g., 5 / 2 would yield 2.5).
"""
from __future__ import division

# To ensure consistent behavior across both versions, developers have two main options

"""
1. Using from __future__ import division in Python 2: This import enables Python
3’s true division, ensuring that dividing integers yields a float.

2. Casting to float: Explicitly casting one or both operands to float guarantees a float
result in both Python 2 and Python 3.
"""

result = 5 / 2

print(result) # prints 2.5 in both Python 2 and Python 3

# Explicitly casting to float
result = float(5) / 2