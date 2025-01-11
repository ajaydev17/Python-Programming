"""
The factory pattern is a creational design pattern that provides an interface for creating
objects in a superclass but allows subclasses to alter the type of objects created. This pattern
is useful when the exact type of object to create is determined at runtime
"""

class Dog:
    def speak(self):
        return "Woof!!!"

class Cat:
    def speak(self):
        return "Meow!!!"

class AnimalFactory:

    @staticmethod
    def create_animal(animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError("Invalid animal type")

animal = AnimalFactory().create_animal('dog')
print(animal.speak())  # Output: Woof!!!