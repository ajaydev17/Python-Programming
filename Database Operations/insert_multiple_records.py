"""
You can insert multiple records using the executemany() method, which allows a
single SQL statement to be executed multiple times with different parameter values. This is
more efficient than executing multiple single insert commands.
"""

import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Inserting multiple records
students = [('Alice', 22), ('Bob', 23), ('Carol', 24)]
cursor.executemany("INSERT INTO students (name, age) VALUES (?, ?)", students)
conn.commit()