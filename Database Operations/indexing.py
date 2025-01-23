"""
An index in a database is a data structure that improves the speed of data retrieval
operations on a table. Indexes allow the database to locate data more quickly, much like an
index in a book. They are commonly used on columns that are frequently searched or used in
WHERE clauses, but they can slow down write operations as they need to be updated when
data changes.
"""

import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Creating an index on the age column of students table
cursor.execute("CREATE INDEX idx_age ON students (age)")
conn.commit()
conn.close()