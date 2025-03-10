"""
Concurrency in Python allows multiple tasks to make progress within the same time
frame by interleaving their execution. Concurrency doesn’t imply simultaneous execution
but rather focuses on tasks making progress without waiting for others to complete fully.

Parallelism, however, means tasks are executed simultaneously, usually across multiple
processors. Due to Python’s GIL, true parallelism with threads is limited. However, using
multiple processes (through the multiprocessing module) achieves parallelism as each
process runs independently with its memory space
"""

import threading
import time

def print_numbers(name):
    for i in range(5):
        print(f"{name} prints: {i}")
        # time.sleep(0.5)


# Create two threads that run concurrently
thread1 = threading.Thread(target=print_numbers, args=("Thread-1",))
thread2 = threading.Thread(target=print_numbers, args=("Thread-2",))

thread1.start()
thread2.start()
thread1.join()
thread2.join()

"""
Here, thread1 and thread2 are two concurrent threads. They take turns printing numbers,
showing how they interleave without running simultaneously.
"""