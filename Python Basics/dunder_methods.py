"""
Dunder methods, also known as magic methods, are special methods in Python with names
that begin and end with double underscores, like __init__, __str__, __len__, etc. They
allow custom behaviors for built-in operations on objects, enabling operator overloading and
providing an interface for Python’s built-in functions.
"""

"""
For example, __init__ initializes an object, __str__ represents an object as a string, and
__add__ enables the use of the + operator.
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2) # Outputs: Point(4, 6)