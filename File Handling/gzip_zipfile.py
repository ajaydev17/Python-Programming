"""
Compressed files reduce file size and are common for backups, archives, and data
transmission. Python’s gzip module allows for .gz files, while zipfile handles .zip files.
These modules provide functions to compress and decompress data, making it easy to store
and retrieve compressed files.
"""

import gzip
import zipfile

# Compressing data using gzip
with gzip.open('example.txt.gz', 'wt') as file:
    file.write('Hello, World!')

# Reading from a .gz file
with gzip.open('example.txt.gz', 'rt') as file:
    content = file.read()
    print(content)



# Compressing data using zipfile
with zipfile.ZipFile('example.zip', 'w') as file:
    file.write('example.txt')

# Reading from a zip file
with zipfile.ZipFile('example.zip', 'r') as file:
    content = file.read('example.txt')
    print(content.decode())

    # # Extracts files to specified directory
    file.extractall('extracted_files')