"""
Python uses an automatic memory management system that includes reference counting
and garbage collection.
"""

"""
Reference Counting: Python keeps track of the number of references to each object
in memory. When an object's reference count drops to zero, the memory occupied by
the object is freed
"""

"""
Garbage Collection: Python’s garbage collector detects and reclaims memory from
objects involved in reference cycles (where objects reference each other, causing their
reference counts to remain above zero). This process is handled by Python’s gc
module.
"""

import gc
# Enable garbage collection
gc.enable()
# Creating a reference cycle
class Node:

    def __init__(self, value):
        self.value = value
        self.next = self


node1 = Node(1)
node2 = Node(2)
node1.next = node2
node2.next = node1

# Collect garbage
gc.collect()