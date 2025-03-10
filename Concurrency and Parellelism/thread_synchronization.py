"""
Thread synchronization ensures that only one thread accesses a shared resource at a
time, preventing data corruption and race conditions. Without synchronization, multiple
threads could modify the same variable simultaneously, leading to inconsistent results.

Python’s Lock object provides a straightforward way to synchronize access to shared
resources. Only one thread can acquire the lock at a time, ensuring that others wait until it’s
released.
"""

import threading

lock = threading.Lock()
counter = 0

def increment_counter():
    global counter
    with lock:
        for i in range(10):
            counter += 1


threads = [threading.Thread(target=increment_counter) for i in range(5)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(f"counter value: {counter}")