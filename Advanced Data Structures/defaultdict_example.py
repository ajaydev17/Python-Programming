"""
defaultdict is like a regular dictionary but with a default value for nonexistent keys, defined
by the default_factory function. It prevents KeyError by automatically assigning a default
value, such as an integer, list, or set, when a new key is accessed. It’s especially helpful when
populating lists or counters by appending values without needing to check if the key exists.

Key Features:
    ● Allows complex data structures as values, such as list, set, or int.
    ● default_factory can be any callable, including custom functions.

Use Cases:
    ● Grouping items by category (e.g., words by their first letter).
    ● Counting occurrences without manual initialization.
"""

from collections import defaultdict

# counting occurrences with defaultdict
occurrences = defaultdict(int)
words = ['apple', 'banana', 'apple', 'orange']

for word in words:
    occurrences[word] += 1

print(occurrences)