"""
re.search scans the entire string for any location where the pattern appears,
making it useful when you want to find a pattern anywhere in the text. In contrast, re.match
only checks the beginning of the string. If the pattern is found anywhere except at the start,
re.match will return None. For instance, if you want to confirm a string starts with "https,"
re.match is ideal; however, for finding occurrences anywhere in the text, re.search is
preferred.
"""

import re

text = 'Python is powerful!!!'

# using re search
search_result = re.search(r'is', text)
print(search_result)    # Output: <re.Match object>

# Using re.match
result_match = re.match(r'is', text)
print(result_match) # Output: None