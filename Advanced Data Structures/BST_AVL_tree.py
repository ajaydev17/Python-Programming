"""
A balanced binary tree is a binary tree structure where the height difference (or
balance factor) between the left and right subtrees of any node is at most one. This balance
ensures efficient O(log n) operations for insertion, deletion, and search. Without balancing,
binary trees can degrade into linked lists, leading to O(n) operations instead of O(log n).
Balanced trees are essential in applications requiring quick data retrieval and updates, like
databases and search engines.

Types of Balanced Trees:
    ● AVL Tree: Self-balancing with specific rotation operations to keep nodes balanced.
    ● Red-Black Tree: Maintains balance through coloring nodes and specific rules for
    insertion and deletion.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left),
                              self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left),
                              self._get_height(y.right))

        return y

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left),
                              self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left),
                              self._get_height(y.right))

        return y

    def insert(self, root, value):
        if not root:
            return Node(value)

        if value < root.data:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        root.height = 1 + max(self._get_height(root.left),
                              self._get_height(root.right))

        # check balance and apply rotation if necessary
        balance = self._get_balance(root)

        # Left-Left Case
        if balance > 1 and value < root.left.data:
            return self._right_rotate(root)

        # Right-Right Case
        if balance < -1 and value > root.right.data:
            return self._left_rotate(root)

        # Left-Right Case
        if balance > 1 and value > root.left.data:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)

        # Right-Left Case
        if balance < -1 and value < root.right.data:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)

        return root