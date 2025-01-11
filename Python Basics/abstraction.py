"""
Abstraction in Python is a programming concept used to hide implementation details and expose only the
essential features of an object or function. It allows you to focus on what an object does instead
of how it does it.

In Python, abstraction can be implemented using abstract classes and abstract methods,
provided by the abc (Abstract Base Classes) module.
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height