"""
any() and all() are functions that test conditions across elements in an iterable

● any() returns True if any element in the iterable is True.
● all() returns True if every element in the iterable is True.
"""

numbers = [0, 1, 2, 3]

print(any(numbers)) # output: True since 1, 2 and 3 are True
print(all(numbers)) # output: False since 0 is False

"""
Use Case: These functions are valuable in situations like data validation or conditional checks
across multiple items, such as ensuring every field in a form is filled (using all()) or checking
if any warning flags are raised (using any()).
"""