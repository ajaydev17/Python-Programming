"""
Circular imports occur when two or more modules depend on each other, directly or
indirectly. Python raises an ImportError in such cases because the interpreter cannot
resolve dependencies. To handle circular imports, you can restructure the code to remove
the dependency loop, use import statements within functions (local imports), or move shared
code to a separate module that both modules can import
"""

# the below code will throw ImportError because of circular imports

# file: module1.py
import module2

def func1():
    module2.func2()

# file: module2.py
import module1

def func2():
    module1.func1()

# To solve the issue, move imports inside functions if they're not required globally
def func1():
    from module2 import func2
    func2()
