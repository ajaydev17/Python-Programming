"""
The seek() method repositions the file cursor to a specified byte offset within the
file, allowing the program to re-read, skip, or revisit specific sections of the file. It has two
parameters: offset (the byte location) and from_what (the reference point: 0 for the start, 1
for the current position, and 2 for the end). Using seek() is valuable when handling large
files, binary data, or implementing file-processing algorithms.
"""

with open('example.txt', 'r') as f:
    f.seek(10)  # Moves cursor to the 10th byte from the beginning
    content = f.read()