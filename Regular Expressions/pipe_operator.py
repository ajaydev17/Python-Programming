"""
The | (pipe) operator represents alternation, similar to a logical "or" in regex
patterns. It allows you to match one of multiple patterns. For instance, cat|dog will match
either "cat" or "dog." This is useful when there are multiple acceptable inputs or variations in
text, allowing you to match any of the alternatives.
"""

import re

text = "cat or dog"
pattern = r'cat|dog'

matches = re.findall(pattern, text)
print(matches) # Output: ['cat', 'dog']