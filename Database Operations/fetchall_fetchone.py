"""
To retrieve all records from a table, you use the SELECT * statement. In Python, this
can be achieved with the cursor.execute function, followed by fetchall() or fetchone()
to retrieve the data.
"""

import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Retrieving all records
cursor.execute("SELECT * FROM students")
records = cursor.fetchall()

for record in records:
    print(record)

conn.close()