"""
: In the multiprocessing module, Lock ensures that only one process accesses a
shared resource at a time, preventing race conditions. Similar to threading.Lock,
multiprocessing.Lock is used to synchronize access to resources across multiple processes.

When a process acquires a lock, other processes attempting to acquire it will be blocked until
it’s released, ensuring consistent access to shared data.
"""

import multiprocessing

def task(lock, value):
    lock.acquire()

    try:
        print(f"Process {value} acquired the lock")
    finally:
        lock.release()

lock = multiprocessing.Lock()
processes = [multiprocessing.Process(target=task, args=(lock, i)) for i in range(5)]

for process in processes:
    process.start()

for process in processes:
    process.join()