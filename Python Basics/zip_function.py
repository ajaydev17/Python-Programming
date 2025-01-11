"""
The zip() function combines multiple iterables (like lists, tuples, etc.) element-wise into
tuples, creating an iterator that yields these tuples. If the input iterables are of unequal
length, zip() stops when the shortest iterable is exhausted.
"""

names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 78]
paired = list(zip(names, scores))
print(paired) # Output: [('Alice', 85), ('Bob', 90), ('Charlie', 78)]

# zip() is particularly useful for tasks like creating dictionaries from two lists:

grades_dict = dict(zip(names, scores))
print(grades_dict) # Output: {'Alice': 85, 'Bob': 90, 'Charlie': 78}