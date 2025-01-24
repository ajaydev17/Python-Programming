"""
To connect to a MySQL database in Python, we typically use the mysql-connectoror PyMySQL library. These libraries provide methods to establish a connection, allowing you to
perform CRUD operations on a MySQL database from within Python.
"""

import mysql.connector

# Connecting to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    database='your_database'
)

cursor = conn.cursor()

# Running a simple query
cursor.execute("SELECT * FROM students")

for row in cursor.fetchall():
    print(row)

conn.close()