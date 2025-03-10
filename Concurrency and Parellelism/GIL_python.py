"""
The GIL in CPython allows only one thread to execute Python bytecode at a time,
even on multi-core processors. This simplifies memory management but prevents true
parallelism in CPU-bound tasks. However, Python threads work well for I/O-bound tasks, as
the GIL releases control during I/O operations.

The GIL’s main impact is on CPU-bound tasks that require heavy computation. In such cases,
using multiple processes with multiprocessing is preferable, as each process has its own
GIL and can run in true parallelism.
"""


import threading
import time

def cpu_intensive_task(name):
    result = 0
    for _ in range(10):
        result += 1
        print(f"{name} prints: {result}")
        time.sleep(0.5)


# start two threads
t1 = threading.Thread(target=cpu_intensive_task, args=("Thread-1",))
t2 = threading.Thread(target=cpu_intensive_task, args=("Thread-2",))

t1.start()
t2.start()

# wait for both threads to finish
t1.join()
t2.join()