"""
Database connection pooling is a technique to manage a pool of database
connections for reuse, enhancing performance by reducing the overhead of creating new
connections. In Python, libraries like psycopg2 for PostgreSQL or mysql-connector offer
pooling options, and connection pools can also be implemented using SQLAlchemy’s
create_engine function with a pool size.
"""

from sqlalchemy import create_engine

# Creating a connection pool with SQLAlchemy
engine = create_engine('sqlite:///example.db', pool_size=5, max_overflow=10)
conn = engine.connect()

# Executing a query
result = conn.execute("SELECT * FROM students")
for row in result:
    print(row)

# Database connection closing.
conn.close()