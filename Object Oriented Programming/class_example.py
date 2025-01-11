"""
In Python, a class is a foundational structure for implementing object-oriented programming
(OOP). It defines a blueprint for creating individual objects with attributes (data) and
methods (functions) that represent the state and behavior of that object type. Classes allow
developers to group related attributes and methods together, which can then be reused and
extended in other parts of the program.
To define a class in Python, you use the class keyword followed by the class name, and then
a colon. The convention is to capitalize class names (e.g., Dog, Person). Inside the class,
methods (functions that
"""

class Dog:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f"{self.name} says woof!!!"

"""
Here, Dog is a class that models a dog's behavior. It has:
● An __init__ method (constructor) to initialize attributes when creating a new Dog
instance.

● A bark method that returns a string when called on a Dog object.
"""