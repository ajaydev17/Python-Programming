# Monkey patching in python refers to dynamically modifying or extending classes or modules at runtime
# This technique is often used to modify third party libraries without altering the original source.
# but it can lead to maintenance challenges if overused, as it modifies the behavior that might affect
# other parts of the code base.


# Monkey patching example

class Dog:
    def bark(self):
        return "Woof!"

# monkey patching to change the behavior
Dog.bark = lambda self: "Bark bark bark!"

dog = Dog()
print(dog.bark())  # Output: Bark bark bark!