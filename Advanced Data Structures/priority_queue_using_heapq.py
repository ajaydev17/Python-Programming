"""
A priority queue is a data structure that returns elements based on priority rather than the
order of insertion. The heapq module implements a binary heap, which is suitable for creating
a min-heap. Elements with the lowest priority (or value) are accessed first, making it useful
for scheduling and load balancing tasks.

Key Features:
    ● heappush() to add items while maintaining the heap structure.
    ● heappop() to remove and return the smallest element.

Use Cases:
    ● Task scheduling where the task with the lowest time gets executed first.
    ● Implementing algorithms like Dijkstra’s shortest path.
"""

import heapq

# Create a min-heap
heap = []

# Add elements to the heap
heapq.heappush(heap, (3, 'medium priority'))
heapq.heappush(heap, (1, 'low priority'))
heapq.heappush(heap, (5, 'high priority'))

# Remove and return the smallest element
print(heapq.heappop(heap)) # Output: (1, 'low priority')