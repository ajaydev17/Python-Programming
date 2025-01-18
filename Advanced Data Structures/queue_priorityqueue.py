"""
queue.PriorityQueue provides a thread-safe priority queue where elements are
dequeued based on priority. It’s commonly used in task scheduling and algorithms like
Dijkstra’s.
"""

from queue import PriorityQueue

pq = PriorityQueue()

pq.put((1, 'task_high')) # Lower number = higher priority
pq.put((3, 'task_low'))
pq.put((2, 'task_medium'))

print(pq.get()) # Output: (1, 'task_high')