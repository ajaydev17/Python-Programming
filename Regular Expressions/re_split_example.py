"""
re.split is a regex-based version of str.split, allowing you to split a string based
on complex patterns rather than a single delimiter. This is helpful for splitting text on
punctuation, multiple spaces, or other patterns. It offers more flexibility than str.split,
which only allows splitting based on a specific delimiter.
"""

import re

text = "apple, orange; banana: pineapple"

result = re.split(r'[;,:\s]+', text)
print(result) # Output: ['apple', 'orange', 'banana', 'pineapple']