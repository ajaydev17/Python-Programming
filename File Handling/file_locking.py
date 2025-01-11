"""
File locking restricts simultaneous access to a file, preventing potential data
corruption in applications with multiple processes or users. Python’s fcntl module
(for Unixbased systems) and msvcrt (for Windows) can lock files, ensuring only one process can write
to a file at a time. Use LOCK_EX for exclusive access and LOCK_UN to release it.
"""

import os
import fcntl

def lock_file(file_path):
    # Open the file in exclusive mode
    with open(file_path, 'a') as f:
        # Acquire the lock
        fcntl.flock(f, fcntl.LOCK_EX)

        # Write to the file
        f.write('This is a test\n')

        # Release the lock
        fcntl.flock(f, fcntl.LOCK_UN)