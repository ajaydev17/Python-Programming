"""
A mixin is a class that provides methods to other classes through inheritance, but it is not
intended to stand alone. Mixins are used to add specific functionality to classes in a modular
way, allowing multiple inheritance without the complexity of multiple full-fledged
superclasses.
"""

class FlyMixin:
    def fly(self):
        return "I'm flying!"

class Bird(FlyMixin):
    pass

class Eagle(FlyMixin):
    pass

class Airplane:
    pass


bird = Bird()
plane = Airplane()
print(bird.fly()) # Outputs: Flying
print(plane.fly()) # Outputs: Flying