# In Python, copying an object can be done either as a shallow copy or a deep copy.

"""
Shallow Copy: Creates a new object, but inserts references to the objects found in the
original. If the original contains nested objects (like lists of lists), the shallow copy only
duplicates the outer container, while the inner objects are still referenced.
"""

"""
Deep Copy: Creates a completely independent copy, duplicating not only the original
object but also any objects that are referenced within it, all the way down to the most
nested levels
"""

"""
Shallow copies are faster and use less memory, but any modification in nested structures of
the original or copied object will reflect in both. copy.copy() is used for shallow copying,
while copy.deepcopy() is used for deep copying.
"""

import copy
original = [[1, 2, 3], [4, 5, 6]]
shallow_copy = copy.copy(original)
deep_copy = copy.deepcopy(original)

original[0][0] = 'Changed'
print(shallow_copy) # Outputs: [['Changed', 2, 3], [4, 5, 6]]
print(deep_copy) # Outputs: [[1, 2, 3], [4, 5, 6]]