"""
A JOIN operation is used to combine rows from two or more tables based on a
related column between them. In Python, you can perform JOIN operations by using SQL
JOIN statements in conjunction with cursor.execute. The JOIN keyword can be INNER
JOIN, LEFT JOIN, RIGHT JOIN, etc., depending on the requirement.
"""

import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Creating tables
cursor.execute("CREATE TABLE IF NOT EXISTS courses (course_id INTEGER PRIMARY KEY, course_name TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS enrollments (student_id INTEGER, course_id INTEGER)")

# Performing a JOIN
cursor.execute('''SELECT students.name, courses.course_name
                    FROM students
 I                  NNER JOIN enrollments ON students.id = enrollments.student_id
                    INNER JOIN courses ON enrollments.course_id =
                    courses.course_id''')

results = cursor.fetchall()

for row in results:
    print(row)
conn.close()