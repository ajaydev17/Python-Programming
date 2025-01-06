"""
Compressed files reduce storage space and transmission time, especially for large
datasets. You can handle compressed files directly by opening them with gzip or bz2
modules, then passing the file objects to JSON or CSV functions

● gzip for JSON: Open the file with gzip.open() in text mode ('wt' for writing, 'rt' for
reading) and pass the file object to json.dump() or json.load().

● gzip for CSV: Open with gzip.open() and use csv.reader() or csv.writer() on the
file object.
"""

import gzip
import json

# JSON with gzip
data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

# writing to compressed JSON
with gzip.open('data.json.gz', 'wt') as f:
    json.dump(data, f)

# reading from compressed JSON
with gzip.open('data.json.gz', 'rt') as f:
    json_data = json.load(f)
    print(json_data)