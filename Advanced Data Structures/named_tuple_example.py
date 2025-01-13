"""
namedtuple allows creating lightweight, immutable data structures with named fields. It’s an
alternative to classes when you only need to store data without behavior, making the code
cleaner and more readable. Unlike regular tuples, fields are accessed by names instead of
indices, improving readability and maintainability.


Key Features:
    ● Provides a human-readable __repr__ for better debugging.
    ● Fields are immutable, so you cannot modify values after creation.

Use Cases:
    ● Storing coordinates, RGB color values, or records where fields are fixed.
    ● Representing small data objects without needing full-fledged classes.
"""

from collections import namedtuple

# creating a Point namedtuple for 2D coordinates
Point = namedtuple('Point', ['x', 'y'])

# creating a Point instance
p = Point(10, 20)

# accessing fields
print(p.x)  # Output: 10
print(p.y)  # Output: 20