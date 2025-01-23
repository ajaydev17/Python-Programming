"""
: CRUD stands for Create, Read, Update, and Delete—four basic operations for
managing data in a database. In Python, CRUD can be implemented by running SQL queries
to insert, fetch, update, and delete data in tables
"""

import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('my_database.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table named 'users'
cursor.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY, name TEXT NOT NULL, email TEXT NOT NULL)''')

# Insert a new user into the 'users' table
cursor.execute("INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com')")

# Fetch all rows from the 'users' table
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

# Update an existing user's email
cursor.execute("UPDATE users SET email = 'alice@example.com' WHERE id = 1")

# Delete a user from the 'users' table
cursor.execute("DELETE FROM users WHERE id = 1")

# Commit the changes and close the connection
conn.commit()
conn.close()