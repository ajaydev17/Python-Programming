"""
Greedy matching captures as much text as possible. In regex, * (zero or more) and +
(one or more) are greedy by default, meaning they will try to match the longest possible
substring that satisfies the pattern. Greedy matches are useful when you want a pattern to
consume all possible characters until the end.
"""

import re

text = "a<content>more content</content>b"
pattern = r'<.*>'

match = re.search(pattern, text)
print(match.group()) # Output: <content>more content</content>