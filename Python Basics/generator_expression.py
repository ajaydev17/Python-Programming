"""
Generator expressions are similar to list comprehensions but differ in that they generate
values on-the-fly rather than creating a list. They are written with parentheses () instead of
square brackets []. This lazy evaluation is memory-efficient, especially for large datasets, as it
only produces items when needed.
"""

numbers = (x ** 2 for x in range(10))

# Print the first 5 values of the generator expression
for _ in range(5):
    print(next(numbers))

"""
In contrast, a list comprehension [x**2 for x in range(10)] would produce all items at
once, consuming more memory. Generators are preferred when you don’t need all elements
at once, such as in large data pipelines.
"""