"""
The __name__ variable in Python is a special built-in variable that Python sets automatically,
depending on how the module is run. If the module is executed directly (e.g.,
my_module.py), __name__ is set to "__main__". When imported into another module,
__name__ holds the module's actual name, not "__main__". This feature allows for control
over code execution within the module, so that specific parts run only if the module is
executed directly, rather than imported. It is particularly useful for testing purposes and
script modularity.
"""

# In a file named my_module.py
def greet():
    print('Hello, World!!')


if __name__ == '__main__':
    greet()    # this runs only when  my_module.py is executed directly


# If imported in another script
# import my_module
# The greet function won't run unless called explicitly