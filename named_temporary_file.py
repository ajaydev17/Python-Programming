"""
Use Python’s tempfile module to create temporary files, which are automatically
deleted when closed. The NamedTemporaryFile() function provides a file-like object that is
accessible by name and ensures the file is removed once the file object is closed or the
program ends, ideal for temporary data storage in multi-user applications.
"""

import tempfile

# create a temporary file
with tempfile.NamedTemporaryFile(delete=True) as tmp_file:
    tmp_file.write(b"Hello, world!")
    print(tmp_file.name)