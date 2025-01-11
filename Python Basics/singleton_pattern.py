"""
The Singleton pattern restricts a class to a single instance, ensuring controlled access to
shared resources. Python supports several ways to implement a Singleton, including
module level variables, metaclasses, and using __new__.

A common approach is to override __new__ to ensure only one instance of the class is
created.
"""

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1 is singleton2) # Outputs: True