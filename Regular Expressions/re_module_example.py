"""
The re module in Python provides tools for working with regular expressions, which
are sequences of characters forming a search pattern. Regex is powerful for searching and
manipulating strings based on complex patterns rather than literal characters. It’s useful for
applications like validating user inputs (emails, phone numbers), searching for keywords, and
even parsing documents. Python’s re module offers various functions such as re.search,
re.match, re.findall, and re.sub, each with specific purposes, helping to efficiently process
and manipulate text.
"""

import re

pattern = r'\d+'
text = 'There are 123 apples and 45 bananas.'
matches = re.findall(pattern, text)
print(matches)  # Output: ['123', '45']