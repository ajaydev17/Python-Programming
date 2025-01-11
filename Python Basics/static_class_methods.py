# In python staticmethod and classmethod are decorators used to define methods that differ in how they
# interact with the class.

# staticmethod: This is a method that does not receive any references to the instance or class
# It behaves like a regular method, but it belongs to the class's namespace.

# classmethod: This is a method receives a reference to the class(cls) as its first argument,
# rather than an instance. It can access and modify the class state but not the instance state.


class MyClass:
    class_variable = 'Class Variable'

    @staticmethod
    def static_method():
        print('This is a static method.')

    @classmethod
    def class_method(cls):
        print(f'This is a class method. Class variable is: {cls.class_variable}')