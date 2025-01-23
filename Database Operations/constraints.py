"""
Constraints are rules applied to database columns to ensure the validity and
integrity of the data. Common constraints include PRIMARY KEY, FOREIGN KEY, UNIQUE, NOT
NULL, and CHECK. They prevent invalid data entry by enforcing rules at the database level,
which helps maintain data consistency and accuracy.
"""

import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Creating a table with constraints
cursor.execute('''CREATE TABLE students (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER CHECK(age >= 0))''')

conn.commit()
conn.close()