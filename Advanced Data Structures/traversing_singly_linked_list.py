"""
Traversing a singly linked list involves iterating from the head node to the end node.
Starting from the head, each node’s data is processed, and then we move to the next node
using the next reference. Traversal continues until a None reference is reached, indicating the
end of the list.
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next