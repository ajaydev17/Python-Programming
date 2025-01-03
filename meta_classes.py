# Metaclasses in python are the 'classes of classes', They define how classes behave, allowing you
# to control the creation and behavior of classes themselves. By default, python's built-in type is the
# metaclass for all classes, but you can create custom metaclasses to control class construction and
# behavior, they are commonly used for enforcing rules on classes, creating APIs or automating class
# generation

class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        # Add a new attribute to all classes created from MyMeta
        attrs['new_attribute'] = 'This is a new attribute'

        # Here, MyMeta metaclass automatically adds a greet method to any class that uses it
        attrs['greet'] = lambda self: f"Hello from {name}"
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=MyMeta):
    pass

obj = MyClass()
print(obj.greet())

# singleton pattern

class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Singleton(metaclass=SingletonMeta):
    pass

obj1 = Singleton()
obj2 = Singleton()
print(obj1 is obj2)  # Output: True


"""
Key Methods of Metaclasses

__new__:

Controls how the class is created.
It is called before the class itself is created.

Arguments:
cls: The metaclass.
name: The name of the class being created.
bases: A tuple of base classes for the class being created.
dct: A dictionary containing the class body.

__init__:

Initializes the created class.
It is called after the class is created.

__call__:

Controls how instances of the class are created (object instantiation).
Allows customization of ClassName() calls.
"""