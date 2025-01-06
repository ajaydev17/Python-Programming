"""
defaultdict is a subclass of Python’s built-in dict, and it simplifies working with keys that
may not be present in the dictionary. With a defaultdict, you specify a factory function (like
int or list) that automatically creates a default value for any new key.
"""

from collections import defaultdict

# Using int as the default factory function
d = defaultdict(int)
d['a'] += 1
d['b'] += 2
print(d)  # Output: defaultdict(int, {'a': 1, 'b': 2})


# Unlike a regular dictionary, defaultdict allows you to initialize missing keys automatically.
# This is especially useful for counters, grouping elements, or appending to lists under each key
# without needing to check key existence manually.