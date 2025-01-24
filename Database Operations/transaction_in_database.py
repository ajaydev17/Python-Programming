"""
Transactions in databases are a sequence of operations performed as a single unit.
They are essential because they ensure data integrity and consistency. If any operation within
a transaction fails, the entire transaction can be rolled back, leaving the database in its
original state. Transactions follow the ACID properties—Atomicity, Consistency, Isolation, and
Durability—ensuring reliable and predictable database operations.
"""

import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('my_database.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Start a transaction
try:
    cursor.execute("INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com')")

    # Perform another operation that may fail
    cursor.execute("INSERT INTO users (name, email) VALUES ('Bob', 'bob@example.com')")

    # Commit the transaction
    conn.commit()


    print("Transaction completed successfully")
except Exception as e:
    # Rollback the transaction if any operation fails
    conn.rollback()
    print("Transaction failed:", e)
finally:
    # Close the connection to the database
    conn.close()
