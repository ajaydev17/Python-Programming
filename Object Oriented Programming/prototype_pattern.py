"""
The prototype pattern is a creational pattern that enables cloning existing objects instead of
creating new instances. This is useful when object creation is costly. Python’s copy module
provides shallow and deep copy methods to implement the prototype pattern.
"""

import copy

class Prototype:
    def __init__(self, value):
        self.value = value

    def clone(self):
        return copy.deepcopy(self)

original = Prototype([1, 2, 3])
cloned = original.clone()
cloned.value.append(4)

print(original.value)  # Output: [1, 2, 3]
print(cloned.value)  # Output: [1, 2, 3, 4]