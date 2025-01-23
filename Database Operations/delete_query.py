"""
To delete a record from a database, you use the DELETE statement with a WHERE
clause to specify which record(s) to remove. In Python, this can be done with
cursor.execute.
"""

import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Deleting a record
cursor.execute("DELETE FROM students WHERE name = 'Bob'")
conn.commit()