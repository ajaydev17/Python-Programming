"""
: re.findall returns all non-overlapping matches of the pattern in a string, yielding a
list of all instances found. It’s particularly useful when you want all occurrences, not just the
first one or a match at the beginning. If the pattern contains capturing groups, findall
returns a list of tuples where each tuple represents the matched groups
"""

import re

text = "The year 2023 is a leap year, unlike 2021."

matches = re.findall(r'\d{4}', text)
print(matches) # Output: ['2023', '2021']

"""
In this case, \d{4} looks for any sequence of four consecutive digits. findall extracts every
match into a list, providing an easy way to retrieve multiple values from a single search.
"""