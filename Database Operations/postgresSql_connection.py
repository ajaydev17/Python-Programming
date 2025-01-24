"""
: In Python, the psycopg2 library is commonly used to connect to PostgreSQL
databases. It provides a Pythonic way to establish a connection and run SQL queries, similar
to MySQL connectors.
"""

import psycopg2

# Connecting to PostgreSQL
conn = psycopg2.connect(
    host='localhost',
    database='your_database',
    user='your_username',
    password='your_password'
)

cursor = conn.cursor()

# Running a query
cursor.execute("SELECT * FROM students")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()