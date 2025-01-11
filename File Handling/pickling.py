"""
Serialization (or pickling) converts Python objects (lists, dictionaries, etc.) into byte
streams using pickle. This allows complex data structures to be saved to a file and later
restored in their original format. Be cautious: loading pickled data from untrusted sources
can be insecure as it can execute arbitrary code during deserialization.
"""

import pickle

# Create a dictionary to be serialized
data = {
    "name": "John Doe",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "New York"
    }
}

# Serialize the dictionary into a byte stream
serialized_data = pickle.dumps(data)

# Save the byte stream to a file
with open("serialized_data.pkl", "wb") as file:
    file.write(serialized_data)


# Restore the dictionary
with open("serialized_data.pkl", "rb") as file:
    restored_data = pickle.load(file)

print(restored_data)