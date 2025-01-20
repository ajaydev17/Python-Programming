"""
re.compile is used to compile a regex pattern into a regex object, which can be
reused efficiently for multiple matches. When you call re.search or re.match without
compile, the regex pattern is recompiled each time, slightly impacting performance,
especially in loops or repetitive tasks. By compiling the regex first, Python avoids recompiling
the pattern and can perform repeated searches quickly.
"""

import re

pattern = re.compile(r'\bPython\b')
text1 = "I love Python programming"
text2 = 'Python is versatile'

match1 = pattern.search(text1)
match2 = pattern.search(text2)

print(match1.group())
print(match2.group())