"""
Memory-mapped file access, enabled by Python’s mmap module, maps a file’s
contents into memory, allowing efficient access to file data without loading the entire file. It’s
suitable for working with very large files, as only the accessed parts are loaded into memory.

● Use Case: Ideal for applications that need to access specific file segments or require
high-performance data access.
"""


import mmap

with open('large_file.txt', 'r') as f:
    mmapped_file = mmap.mmap(f.fileno(), 0)  # Maps entire file
    print(mmapped_file.readline())  # Reads a line
    mmapped_file.close()

