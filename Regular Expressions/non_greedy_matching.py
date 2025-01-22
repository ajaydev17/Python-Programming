"""
Non-greedy (or lazy) matching captures the smallest possible amount of text to
satisfy the pattern. Adding ? after * or + makes these quantifiers non-greedy. This is useful
when you want to match the minimal text necessary, especially when multiple occurrences
exist and you want to capture each individually.
"""

import re

text = "a<content>more content</content>b"
pattern = r'<.*?>'

match = re.search(pattern, text)
print(match.group()) # Output: <content>

"""
Here, <.*?> matches only the first <content>, as it stops matching as soon as it finds a >,
demonstrating non-greedy matching.
"""