"""
A hash table can be implemented using a list of lists (or dictionaries) where each
key-value pair is stored in a specific "bucket" determined by a hash function. When
implementing a hash table, consider how to handle collisions (e.g., with chaining or open
addressing).
"""

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        # Implement a hash function to determine the bucket index
        return hash(key) % self.size

    def insert(self, key, value):
        bucket_index = self._hash(key)
        for i, kv in enumerate(self.table[bucket_index]):
            if kv[0] == key:
                self.table[bucket_index][i] = (key, value)
                return
        self.table[bucket_index].append((key, value))

    def retrieve(self, key):
        bucket_index = self._hash(key)
        for kv in self.table[bucket_index]:
            if kv[0] == key:
                return kv[1]
        return None

    def delete(self, key):
        bucket_index = self._hash(key)
        for i, kv in enumerate(self.table[bucket_index]):
            if kv[0] == key:
                del self.table[bucket_index][i]
                return
        raise KeyError(f"Key '{key}' not found in the hash table.")