"""
The queue module provides thread-safe queues that support FIFO (Queue class) and LIFO
(LifoQueue class) ordering. FIFO queues process items in the order of their arrival, while LIFO
queues follow a stack-like approach, processing the latest added items first.

Key Features:
    ● Thread-safe for multithreaded applications.
    ● Blocks by default until space is available or items are present.

Use Cases:
    ● Task queues where tasks are added and processed in sequence
    ● Stacks for managing function calls in algorithms.
"""

from queue import Queue, LifoQueue

# Create a FIFO queue
fifo_queue = Queue()

# Add items to the queue
fifo_queue.put('Task 1')
fifo_queue.put('Task 2')
fifo_queue.put('Task 3')

# Remove items from the queue
print(fifo_queue.get())  # Output: Task 1
print(fifo_queue.get())  # Output: Task 2


# Create a LIFO queue
lifo_queue = LifoQueue()

# Add items to the queue
lifo_queue.put(1)
lifo_queue.put(2)

# Remove items from the queue (in reverse order of addition)
print(lifo_queue.get())  # Output: 2
print(lifo_queue.get())  # Output: 1