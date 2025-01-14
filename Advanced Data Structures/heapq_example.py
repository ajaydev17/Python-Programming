"""
The heapq module provides an implementation of the heap queue algorithm, also
known as the priority queue algorithm. It supports a min-heap, where the smallest element
can be accessed efficiently. The most commonly used functions in heapq are heappush() for
adding an element and heappop() for removing the smallest element.

Key Operations:
    ● heappush(heap, item): Adds an item to the heap.
    ● heappop(heap): Removes and returns the smallest item from the heap.
"""

import heapq

# Create a min-heap
heap = []

# Add elements to the heap
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 5)

# Remove and return the smallest element
print(heapq.heappop(heap))  # Output: 1