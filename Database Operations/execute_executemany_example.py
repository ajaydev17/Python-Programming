"""
In Python’s sqlite3 module, the execute method allows you to run a single SQL
statement, while executemany lets you execute a single SQL command multiple times with
different parameters. execute is ideal for operations like creating tables or inserting a single
record, while executemany is more efficient when you need to insert multiple records or run
the same query with different data.
"""

import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Using execute
cursor.execute("INSERT INTO students (name, age) VALUES ('Bob', 22)")

# Using executemany
data = [('Carol', 23), ('Dave', 24)]

cursor.executemany("INSERT INTO students (name, age) VALUES (?, ?)", data)
conn.commit()