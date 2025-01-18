"""
Dynamic imports allow you to import modules at runtime, which is useful when the module
name isn’t known until execution. The __import__ function is a built-in way to import a
module by name, but importlib provides a more flexible and recommended approach for
dynamic imports, especially for Python 3. importlib.import_module is preferable for
readability and compatibility with future versions.
"""

# Using importlib to dynamically import a module
import importlib

module_name = "math"
math_module = importlib.import_module(module_name)

print(math_module.sqrt(25)) # Output: 5.0

"""
Dynamic imports are beneficial in situations requiring flexible imports, such as plugin
systems or applications that need to load modules based on user input.
"""