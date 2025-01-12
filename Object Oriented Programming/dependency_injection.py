"""
Dependency injection is a design pattern in which an object receives other objects it
depends on, rather than creating them itself. This promotes loose coupling, as dependencies
are injected from outside. In Python, dependency injection can be implemented by passing
dependencies through the constructor or method arguments.
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