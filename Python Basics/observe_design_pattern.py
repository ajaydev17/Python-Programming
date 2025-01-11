"""
The Observer pattern is a behavioral design pattern where an object (subject) maintains a list
of dependents (observers) that it notifies of any state changes. This pattern is commonly
used in event-driven applications.

In Python, it can be implemented by having an Observer class with a method that updates
the observer and a Subject class that manages the list of observers and notifies them of
changes.
"""

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, message):
        for observer in self._observers:
            observer.update(message)

class Observer:
    def update(self, message):
        print(f"Received message: {message}")

subject = Subject()
observer1 = Observer()
subject.attach(observer1)

subject.notify("New data available") # Outputs: Received message: New data available