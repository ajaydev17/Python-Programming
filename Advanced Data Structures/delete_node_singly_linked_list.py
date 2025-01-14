"""
Deleting a node from a singly linked list requires adjusting the next reference of the
preceding node to skip the node to be deleted. If the node is the head, the head reference is
updated. For intermediate nodes, the reference of the previous node is updated to point to
the node after the one to be deleted.

Steps:
    1. Identify the node to delete.
    2. Update the next pointer of the previous node.
    3. If deleting the head, update the head reference.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def delete(self, value):
        if not self.head:
            return

        if self.head.data == value:
            self.head = self.head.next
            if not self.head:
                self.tail = None
            return

        current = self.head
        while current.next and current.next.data != value:
            current = current.next

        if current.next:
            current.next = current.next.next
            if not current.next:
                self.tail = current
