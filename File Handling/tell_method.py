"""
The tell() method returns the current position of the file cursor, which is the byte
location from the start of the file. Each time data is read or written, the cursor advances, and
tell() can provide this exact location. This information is helpful when tracking how much
of a file has been read or written, debugging, or creating file checkpoints in larger files where
different sections are processed at different times
"""

with open('example.txt', 'r') as f:
    f.seek(10)  # Move the cursor to the 10th byte
    position = f.tell()
    print(f"Current position: {position}")