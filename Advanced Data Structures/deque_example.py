"""
A deque (double-ended queue) supports fast appends and pops from both ends, unlike lists
where these operations on the start of the list are inefficient. deque is implemented with a
doubly-linked list, allowing it to perform O(1) operations on both ends, making it suitable for
situations where fast insertion or removal is needed on either side.

Key Features:
● appendleft() and popleft() methods for left-side manipulation.
● rotate() method, which can shift all elements by a specified number of positions.

Use Cases:
● Implementing both FIFO and LIFO queues.
● Sliding window algorithms that require adding and removing elements from both
ends.
"""

from collections import deque

# Creating a deque with initial elements
deque_obj = deque(['a', 'b', 'c'])

# Adding elements to the right end
deque_obj.append('d')
deque_obj.append('e')
print(deque_obj)  # Output: deque(['a', 'b', 'c', 'd', 'e'])

# Adding elements to the left end
deque_obj.appendleft('x')
deque_obj.appendleft('y')
print(deque_obj)  # Output: deque(['y', 'x', 'a', 'b', 'c', 'd', 'e'])

# Removing elements from the right end
print(deque_obj.pop())  # Output: e
print(deque_obj)  # Output: deque(['y', 'x', 'a', 'b', 'c', 'd'])

# Removing elements from the left end
print(deque_obj.popleft())  # Output: y
print(deque_obj)  # Output: deque(['x', 'a', 'b', 'c', 'd'])

# Rotating elements
deque_obj.rotate(2)  # Move the last two elements to the front
print(deque_obj)  # Output: deque(['c', 'd', 'x', 'a', 'b'])

deque_obj.rotate(-1)  # Move the first element to the end
print(deque_obj)  # Output: deque(['d', 'x', 'a', 'b', 'c'])