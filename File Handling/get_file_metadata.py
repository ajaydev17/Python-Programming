"""
File metadata provides details about a file’s properties. Using the os module, you can
retrieve metadata like file size, creation time, and last modification time.

● File Size: os.path.getsize() returns the file’s size in bytes.

● Modification Time: os.path.getmtime() returns the last modification time as a
timestamp, which can be converted into a readable format using time.ctime().
"""

import os
import time

filename = 'example.txt'

# Get file size in bytes
file_size = os.path.getsize(filename)
print(f"File size: {file_size} bytes")

# Get last modification time
modification_time = os.path.getmtime(filename)
last_modification_time = time.ctime(modification_time)
print(f"Last modification time: {last_modification_time}")