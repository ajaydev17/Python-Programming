"""
sqlite3 is a built-in module in Python that allows you to work with SQLite
databases. SQLite is a lightweight, disk-based database that doesn't require a separate server
process, making it ideal for embedded applications or small projects. The sqlite3 module
provides a way to create and interact with databases using SQL commands, making it a
suitable choice for managing structured data in a simple and efficient way.
"""

import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('my_database.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table called "users" with columns "id" (integer), "name" (text), and "email" (text)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
''')

# Insert a new user into the "users" table
cursor.execute('''
    INSERT INTO users (name, email)
    VALUES ('Alice', 'alice@example.com')
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

"""
In the above code, we use sqlite3.connect to create or open a database file. We execute
SQL commands to create tables and insert data, and finally, we save the changes using
commit().
"""