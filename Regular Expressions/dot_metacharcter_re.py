"""
The dot (.) metacharacter matches any character except a newline. It’s useful for
matching any single character when the content in between is not fixed, but should be
limited to a single line. To allow a dot to also match newlines, you can set the re.DOTALL flag,
which lets the dot match newline characters as well.
"""

# dot metacharacter use

import re

pattern = r'c.t'
text = "cat, cut, cot, czt, c\t!"
matches = re.findall(pattern, text)
print(matches) # Output: ['cat', 'cut', 'cot', 'czt']