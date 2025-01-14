"""
Stacks are LIFO (Last-In-First-Out) data structures, typically implemented with a list in
Python. Stacks are used in scenarios where you need to keep track of recently accessed data,
such as maintaining a call stack in recursive functions or implementing an undo mechanism.

Key Features:
    ● append() for pushing items.
    ● pop() for removing the last item.

Use Cases:
    ● Function call tracking.
    ● Implementing browser back-button functionality.
"""


# Example usage of a stack
stack = []

# Push items onto the stack
stack.append(1)
stack.append(2)
stack.append(3)

# Pop items from the stack
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 2
print(stack.pop())  # Output: 1