"""
CSV files sometimes contain cells with multi-line text. The csv module allows
handling multi-line fields by using the quotechar and quoting=csv.QUOTE_ALL settings,
which ensure that multi-line cells are enclosed in quotes.

● Writing Multi-line Records: Use csv.writer() with quoting=csv.QUOTE_ALL to
enclose each cell in quotes, preserving newlines within cells.

● Reading Multi-line Records: The csv.reader() will automatically handle cells with
multi-line content if they’re properly quoted.
"""

import csv

data = [
    [
        "Name",
        "Address\nLine 1\nLine 2",
        "Phone",
    ],
    [
        "John Doe",
        "123 Main St\nAnytown, USA",
        "555-1234",
    ]
]

# writing multi-line records with quotes
with open("multi_line_records.csv", "w", newline="") as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    writer.writerows(data)

# reading from the CSV
with open("multi_line_records.csv", "r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)