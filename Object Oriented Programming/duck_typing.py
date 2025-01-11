"""
Duck typing in Python is a concept related to polymorphism, where the type of an object is
determined by its behavior (methods and properties) rather than its class inheritance. If an
object implements the expected behavior, it can be used in place of other objects, even if it
doesn't inherit from a particular class.
"""

class Duck:

    def quack(self):
        return "Quack!"

class Dog:

    def quack(self):
        return "Woof!"

def make_it_quack(obj):
    return obj.quack()

duck = Duck()
dog = Dog()

print(make_it_quack(duck))  # Output: Quack!
print(make_it_quack(dog))   # Output: Woof!