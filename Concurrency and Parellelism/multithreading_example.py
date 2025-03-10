"""
Multithreading in Python enables concurrent execution of multiple threads within
the same process. Each thread shares the same memory, making context switching
lightweight. However, due to the GIL, threads in Python are generally suited for I/O-bound
tasks, where threads wait for external resources.

For CPU-bound tasks, threads don’t achieve true parallelism due to GIL limitations. However,
for I/O-bound operations (like file or network operations), threads are beneficial as they can
continue execution while waiting for I/O to complete.
"""

import threading
import time


def fetch_data():
    print("Fetching data...")
    time.sleep(2)
    print("Data fetched")


def process_data():
    print("Processing data...")
    time.sleep(3)
    print("Data processed")


# Creating two threads for I/O-bound tasks
thread1 = threading.Thread(target=fetch_data)
thread2 = threading.Thread(target=process_data)


thread1.start()
thread2.start()

thread1.join()
thread2.join()