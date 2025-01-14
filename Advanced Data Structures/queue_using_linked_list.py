"""
A queue implemented with a linked list maintains pointers to the front and rear nodes. This
allows adding and removing items in constant time (O(1)), even as the queue grows. This
approach is efficient and avoids the resizing overhead associated with array-based queues
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None



class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if not self.front:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.front:
            return None
        data = self.front.data
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return data