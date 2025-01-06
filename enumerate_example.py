"""
The enumerate() function adds a counter to each item in an iterable, returning a sequence
of (index, item) tuples. It simplifies tasks where both the element and its index are
required in a loop, eliminating the need for a manual counter.
"""

items = ['a', 'b', 'c', 'd', 'e', 'f']

# Using enumerate() to get both index and item
for index, item in enumerate(items):
    print(f"Index: {index}, Item: {item}")


"""
Use Case: enumerate() is useful in processing elements with context, such as labeling rows
in a table, creating labeled lists, or tracking element positions in data analysis.
"""