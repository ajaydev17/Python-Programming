"""
OrderedDict maintains the insertion order of keys, which standard dictionaries before
Python 3.7 did not guarantee. This makes it suitable when order-sensitive operations are
required, like in caching algorithms where the order of insertion may determine which item
to remove first.

Key Features:
    ● Preserves insertion order.
    ● Has methods like move_to_end() to change the position of elements.

Use Cases:
    ● Creating an LRU (Least Recently Used) cache.
    ● Tracking items in the order they were added.
"""

from collections import OrderedDict

# Creating an OrderedDict
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3

# Accessing items by their order
for key in ordered_dict:
    print(key, ordered_dict[key])