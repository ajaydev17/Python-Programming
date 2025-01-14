"""
Python's heapq module only provides a min-heap by default, but a max-heap can be
simulated by inserting negative values. By inverting the values, the largest element becomes
the smallest in terms of absolute value, which allows us to achieve max-heap behavior
"""

import heapq

# Create a max-heap
max_heap = []

# Add elements to the max-heap
heapq.heappush(max_heap, -1 * 3)
heapq.heappush(max_heap, -1 * 1)
heapq.heappush(max_heap, -1 * 5)

# Remove and return the largest element
print(-1 * heapq.heappop(max_heap)) # Output: (5, 'high priority')