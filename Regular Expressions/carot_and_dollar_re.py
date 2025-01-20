"""
Anchors help match patterns based on specific positions in a string. ^ matches the
beginning of a string, ensuring the pattern appears at the start, while $ matches the end,
ensuring the pattern appears only at the string's end. These are essential for patterns like
validating email addresses or URLs, where the string must follow strict positioning rules.
"""

import re

text = "Hello World!"

pattern_start = r'^Hello'
pattern_end = r'World!$'

print(re.search(pattern_start, text)) # Output: <re.Match object>
print(re.search(pattern_end, text)) # Output: <re.Match object>

"""
Here, ^Hello requires "Hello" at the beginning, while World!$ confirms it ends with "World!"
"""