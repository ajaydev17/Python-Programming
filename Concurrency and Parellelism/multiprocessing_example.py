"""
The multiprocessing module allows Python programs to bypass the GIL by
creating separate processes, each with its memory space. This enables true parallelism,
making it ideal for CPU-bound tasks.

The Process class allows you to create a new process, and each process runs independently.
The Pool class manages multiple processes, distributing tasks across them for efficient
"""

import multiprocessing

def cpu_task():
    # Perform CPU-bound task
    result = sum(range(10000000))
    return result


# create and start a process
process = multiprocessing.Process(target=cpu_task)
process.start()
process.join()