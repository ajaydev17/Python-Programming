"""
A custom priority queue can be implemented by creating a class with methods
for enqueueing and dequeueing based on priority. By using the heapq module, we can
manage elements in a way that always provides access to the item with the highest priority
(or lowest numerical value).
"""

import heapq

class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item, priority):
        heapq.heappush(self.queue, (priority, item))

    def dequeue(self):
        return heapq.heappop(self.queue)[1]

    def is_empty(self):
        return len(self.queue) == 0

pq = PriorityQueue()

# enqueue operations
pq.enqueue('Task 1', 1)
pq.enqueue('Task 2', 3)
pq.enqueue('Task 3', 2)

# dequeue operations
print(pq.dequeue())  # Output: Task 1
print(pq.dequeue())  # Output: Task 2
print(pq.dequeue())  # Output: Task 3

print(pq.is_empty())  # Output: True