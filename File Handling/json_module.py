"""
JSON (JavaScript Object Notation) is a text-based format used for representing
structured data. Python’s json module offers a way to store dictionaries, lists, and other
serializable data structures in JSON format. JSON data is easy for humans to read and widely
used in configurations, data exchange between applications, and APIs.

● Writing to JSON: Use json.dump() to write data to a file. The file must be opened in
text mode ('w').
● Reading from JSON: Use json.load() to parse JSON data from a file. The file should
be opened in text mode ('r').
"""

import json

# Writing to JSON
data = {
    'name': 'John Doe',
    'age': 30,
    'cities': ['New York', 'London', 'Tokyo']
}

# Writing to JSON file
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)

# Reading from JSON
with open('data.json', 'r') as infile:
    json_data = json.load(infile)

print(json_data)  # Output: {'name': 'John Doe', 'age': 30, 'cities': ['New York', 'London', 'Tokyo']}

# Converting JSON to Python dictionary
json_string = '{"name": "Alice", "age": 25, "cities": ["New York", "London", "Tokyo"]}'
python_dict = json.loads(json_string)

print(python_dict)  # Output: {'name': 'Alice', 'age': 25, 'cities': ['New York', 'London', 'Tokyo']}

# Converting Python dictionary to JSON
python_dict = {
    'name': 'Bob',
    'age': 28,
    'cities': ['New York', 'London', 'Tokyo']
}
json_string = json.dumps(python_dict)

print(json_string)  # Output: '{"name": "Bob", "age": 28, "cities": ["New York", "London", "Tokyo"]}'


