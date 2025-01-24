"""
To update a record, you use the UPDATE SQL statement with a WHERE clause to
specify the condition. In Python, this is done using cursor.execute.
"""

import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Updating a record
cursor.execute("UPDATE students SET age = 25 WHERE name = 'Alice'")
conn.commit()
conn.close()