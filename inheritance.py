# Inheritance in python is a feature of object-oriented programming that allows a class (Child class)
# to inherit attributes and methods from another class (parent class). This promotes code reuse and hierarchy.
# This child class can override or extend the functionality of the parent class

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"