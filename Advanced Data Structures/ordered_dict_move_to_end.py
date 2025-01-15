"""
The move_to_end() method in OrderedDict moves a specified key to either the end
or the beginning of the dictionary, depending on the last parameter. By default, last=True,
moving the key to the end. If last=False, it moves the key to the beginning. This is
particularly useful when implementing an LRU (Least Recently Used) cache, where the least
recently accessed item is moved to the end and evicted when the cache limit is reached.
"""

from collections import OrderedDict

# LRU cache example using move_to_end()
cache = OrderedDict()
cache['a'] = 1
cache['b'] = 2

# moves 'a' to the end, treating it as recently accessed
cache.move_to_end('a')

# print the cache
print(cache)