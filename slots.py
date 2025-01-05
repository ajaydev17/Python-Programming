"""
The __slots__ attribute in Python restricts a class to only predefined attributes, preventing
the creation of arbitrary new attributes and reducing memory usage. By defining __slots__,
you explicitly specify which attributes the class can have.
"""

# Using __slots__ enforces attribute constraints and improves memory efficiency.

class Person:
    __slots__ = ['name', 'age']

    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person('Alice', 29)
person.name = ''
# person.height = 170  # This will raise a TypeError: 'Person' object has no attribute 'height'