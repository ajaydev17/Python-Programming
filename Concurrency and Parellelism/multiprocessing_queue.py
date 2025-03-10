"""
The Queue class in the multiprocessing module provides a thread- and proces-safe way
to share data between processes. A Queue allows multiple processes to send and
receive messages in a FIFO (First In, First Out) manner, making it ideal for inter-process
communication.
Each process can put items into the queue with put() and retrieve them with get(),
ensuring data integrity while enabling parallel execution.
"""

import multiprocessing

def producer(queue):
    for i in range(5):
        queue.put(i)
        print(f"Producer put: {i}")


def consumer(queue):
    while True:
        item = queue.get()
        print(f"Consumer got: {item}")

        if item is None:
            break

queue = multiprocessing.Queue()

producer_process = multiprocessing.Process(target=producer, args=(queue,))
consumer_process = multiprocessing.Process(target=consumer, args=(queue,))

producer_process.start()
producer_process.join() # Wait for producer to finish before consumer starts

consumer_process.start()
consumer_process.join() # Wait for consumer to finish