"""
A package in Python is a way to organize related modules into a directory hierarchy, helping
manage and structure code effectively, especially in larger projects. A package contains an
__init__.py file, which can be empty or contain initialization code for the package. Modules
are individual .py files, whereas packages are directories containing one or more modules (or
even sub-packages).
"""

# Directory structure
# my_package/
# ├── __init__.py
# ├── module1.py
# └── module2.py


# module1.py
def function1():
    return "Function 1"


# Using the package in another file
# from my_package import module1
# print(module1.function1()) # Output: Function 1