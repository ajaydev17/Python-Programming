"""
To remove duplicates from an unsorted linked list, you can use a set to track
encountered values. By iterating through the list and checking for duplicates, you can adjust
pointers to remove any repeated nodes in O(n) time.
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def remove_duplicates(self):
        current = self.head
        previous = None
        has_seen = set()

        while current:
            if current.data in has_seen:
                previous.next = current.next
            else:
                has_seen.add(current.data)
                previous = current

            current = current.next