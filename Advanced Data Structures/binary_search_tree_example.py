"""
A Binary Search Tree (BST) is a binary tree with nodes arranged so that each left
child is less than its parent and each right child is greater than its parent. Key operations
include insertion, searching, and deletion, all of which generally have O(log n) time
complexity in a balanced BST.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None

    def _insert_recursive(self, root, value):
        if value < root.data:
            if not root.left:
                root.left = Node(value)
            else:
                self._insert_recursive(root.left, value)
        else:
            if not root.right:
                root.right = Node(value)
            else:
                self._insert_recursive(root.right, value)

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _search_recursive(self, root, value):
        if not root:
            return False
        elif value < root.data:
            return self._search_recursive(root.left, value)
        elif value > root.data:
            return self._search_recursive(root.right, value)
        else:
            return True

    def search(self, value):
        return self._search_recursive(self.root, value)
