"""
A process pool manages a group of worker processes to which tasks can be
submitted for parallel execution. Pool simplifies task distribution across processes, ideal for
executing many tasks simultaneously without manually managing each process.

The map() function in Pool applies a function to each item in an iterable, distributing work
across processes for parallel computation.
"""

from multiprocessing import Pool

def square(x):
    return x * x


# Create a pool of 5 processes
with Pool(5) as p:
    # Distribute the work across 5 processes
    result = p.map(square, [1, 2, 3, 4, 5])

print(result)  # Output: [1, 4, 9, 16, 25]