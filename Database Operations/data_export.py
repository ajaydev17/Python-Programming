"""
For large data exports, it's efficient to retrieve data in chunks rather than loading
everything into memory. This can be achieved with methods like fetchmany() or
SQLAlchemy’s yield_per for chunked results, then writing each chunk to a file.
"""

import sqlite3

import csv
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Exporting data in chunks
with open('students_export.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    cursor.execute("SELECT * FROM students")

    while True:
        rows = cursor.fetchmany(100) # Fetch in chunks of 100
        if not rows:
            break
        writer.writerows(rows)

conn.close()