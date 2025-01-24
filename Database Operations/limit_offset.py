"""
Pagination divides large result sets into manageable pages. This can be
implemented by using SQL LIMIT and OFFSET clauses. SQLAlchemy also provides methods
to achieve pagination through query slicing.
"""

import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Fetching records in pages of 10
page = 1
page_size = 10
offset = (page - 1) * page_size
cursor.execute("SELECT * FROM students LIMIT ? OFFSET ?", (page_size, offset))

print(cursor.fetchall())
conn.close()