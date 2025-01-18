"""
The hashlib library provides tools to generate hashes, including the SHA-256 algorithm,
which creates a unique, fixed-size identifier for any input data. This is useful for creating
reproducible identifiers for objects, ensuring uniqueness and consistency.
"""

import hashlib

def generate_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

# Generate SHA-256 hash for a string
hash_value = generate_hash("unique_identifier")
print("SHA-256 Hash:", hash_value)