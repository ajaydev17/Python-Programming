"""
shelve is a Python module that allows you to persistently store Python objects (like
dictionaries) in a file-backed dictionary-like structure. Unlike pickle, which serializes entire
objects, shelve gives you dictionary-like access to stored data.

● Writing Data: You can store data under unique keys, just as you would with a
dictionary.

● Reading Data: Data can be accessed directly using keys, without deserializing the
entire database.
"""

import shelve

# Open a shelve database
with shelve.open('shelved_data') as db:
    # Store data
    db['name'] = 'John Doe'
    db['age'] = 30

# retrieve data with shelve
with shelve.open('shelved_data') as db:
    print(db['name'])  # Output: John Doe
    print(db['age'])   # Output: 30