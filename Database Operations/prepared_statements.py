"""
A prepared statement is a parameterized SQL statement where placeholders are
used instead of directly embedding values. Prepared statements improve security by
preventing SQL injection attacks, as user inputs are treated as data rather than part of the
SQL query. They also enhance performance by allowing the database to reuse execution
plans for the statement.
"""

import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Using a prepared statement
name = 'Alice'
cursor.execute("SELECT * FROM students WHERE name = ?", (name,))
print(cursor.fetchall())

# Using a parameterized query with placeholders
conn.close()