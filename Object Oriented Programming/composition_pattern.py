"""
Composition is a design principle where one class contains an instance of another class to
reuse code, rather than inheriting from it. It’s useful when the relationship between classes is
best described as "has-a" rather than "is-a."
"""

class Engine:
    def start(self):
        return "Engine started."

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        return self.engine.start()

engine = Engine()
car = Car(engine)
print(car.start())  # Outputs: Engine started.