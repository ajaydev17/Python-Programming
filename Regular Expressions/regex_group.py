"""
Groups capture specific sections of a pattern, making it easier to extract and work
with parts of a match. Enclosing parts of a pattern in parentheses () creates a capturing
group. Each group is numbered sequentially, and groups can be accessed by their position.
Grouping is especially helpful in complex patterns where you want to isolate parts of the
match.
"""

import re

text = "Name: Alice, Age: 25"
pattern = r'Name: (\w+), Age: (\d+)'

match = re.search(pattern, text)

name = match.group(1) # "Alice"
age = match.group(2) # "25"

print(f"Name: {name}, Age: {age}")

"""
Here, (\w+) captures "Alice," and (\d+) captures "25" as individual groups, making it easier to
retrieve these values separately.
"""