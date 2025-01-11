"""
super() is a built-in function used to call a method from the superclass in a subclass. It’s
especially useful in multiple inheritance and when dealing with overridden methods.
super() allows you to refer to the superclass without directly naming it, which makes the
code more flexible and maintainable.
"""

class Animal:
    def make_sound(self):
        print("Animal makes a sound.")

class Dog(Animal):
    def make_sound(self):
        super().make_sound()  # Calls the make_sound() method from the superclass
        print("Dog barks.")