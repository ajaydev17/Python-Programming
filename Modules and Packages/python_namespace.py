"""
A namespace in Python is a mapping between names and objects, ensuring that each name
is unique within its scope. Different namespaces exist for functions, classes, and modules.
Modules and packages use namespaces to organize and encapsulate code, avoiding conflicts
with other parts of the codebase. Each module has its own namespace, so two modules can
have functions with the same name without conflict.
"""

# module1.py
def func():
    print('function in module1')

# module2.py
def func():
    print('function in module2')

# main.py
import module1
import module2

module1.func()  # Output: Function in module1
module2.func()  # Output: Function in module2