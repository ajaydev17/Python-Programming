"""
The csv module simplifies handling of CSV (Comma-Separated Values) files, which
store tabular data in plain text. This format is commonly used for data export and import.

● Writing CSV: Use csv.writer() to create a writer object and writer.writerow() or
writer.writerows() to write rows of data.
● Reading CSV: Use csv.reader() to read CSV data, which allows you to iterate over
rows easily. For dictionary-based access, csv.DictReader and csv.DictWriter are
useful.
"""

import csv

# Writing to CSV
with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Age', 'City'])
    writer.writerows([('Alice', 29, 'New York'), ('Bob', 32, 'London')])

# Reading from CSV
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    for row in reader:
        name, age, city = row
        print(f"Name: {name}, Age: {age}, City: {city}")