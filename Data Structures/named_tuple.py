"""
A namedtuple is a factory function in the collections module that allows creating tuples
with named fields, making them more readable than standard tuples. Named tuples
combine the simplicity and memory efficiency of tuples with the readability of named fields.
"""

from collections import namedtuple

# Creating a named tuple called 'Person' with fields 'name' and 'age'.
Person = namedtuple('Person', ['name', 'age'])

# Creating a Person instance with 'Alice' and 29 as the values.
alice = Person('Alice', 29)

# Accessing the values of the Person instance using the field names.
print(alice.name)  # Output: Alice
print(alice.age)  # Output: 29

"""
Use Case: Named tuples are helpful for representing simple structured data like coordinates,
records, or database rows, where fields have specific names. They improve code readability
and maintainability by allowing attribute-like access (p.x instead of p[0]).
"""