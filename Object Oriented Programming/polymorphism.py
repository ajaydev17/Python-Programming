"""
Polymorphism allows different classes to be used with a common interface or method name.
In Python, polymorphism can be achieved through method overriding (having different
implementations of the same method in subclasses) and operator overloading (customizing
behavior for built-in operators).
"""

class Bird:
    def fly(self):
        return "Flying in the sky"

class Airplane:
    def fly(self):
        return "Flying through the air"

def flying_thing(flyer):
    print(flyer.fly())


flying_thing(Bird())
flying_thing(Airplane())