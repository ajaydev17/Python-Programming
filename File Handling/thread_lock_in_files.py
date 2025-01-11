"""
: Concurrent file access requires synchronization to avoid conflicts. Using locks with
Python’s threading or multiprocessing modules prevents multiple threads or processes
from writing to a file at the same time.

● Using Locks: A Lock() object ensures that only one thread can access the file at any
given time.
"""

import threading

lock = threading.Lock()

def write_to_file(filename, data):
    with lock:
        with open(filename, 'a') as file:
            file.write(data + "\n")


thread_1 = threading.Thread(target=write_to_file, args=('data.txt', 'Thread 1 data'))
thread_2 = threading.Thread(target=write_to_file, args=('data.txt', 'Thread 2 data'))

thread_1.start()
thread_2.start()

thread_1.join()
thread_2.join()