"""
A weakref (weak reference) allows an object to be referenced without preventing it from
being garbage-collected. This is useful when you need to reference objects without affecting
their lifecycle, such as caching and circular references in data structures.
"""

import weakref

class MyClass:

    def __del__(self):
        print("MyClass instance deleted")

obj = MyClass()
weak_ref = weakref.ref(obj)

# Accessing the referenced object
print(weak_ref())  # Output: <__main__.MyClass object at 0x7f5415066200>

# Deleting the referenced object
del obj

# Accessing the referenced object (weak reference is now broken)
print(weak_ref())  # Output: None

