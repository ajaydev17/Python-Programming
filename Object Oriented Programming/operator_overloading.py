"""
Operator overloading allows you to define custom behavior for Python's built-in operators
(like +, -, *, etc.) in your own classes. By overriding special methods, also known as "magic
methods" (like __add__ for +, __sub__ for -), you can define how these operators work with
instances of your class. Operator overloading is useful for making custom objects behave like
built-in types, which can make code using these objects more intuitive.
"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"