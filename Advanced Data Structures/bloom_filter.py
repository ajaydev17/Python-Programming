"""
A Bloom Filter is a probabilistic data structure used for fast set membership checks
with false positives but no false negatives. It uses multiple hash functions and a bit array.
"""

class BloomFilter:
    def __init__(self, size):
        self.size = size
        self.bit_array = [False] * size

    def _hash(self, value, i):
        return (hash(value) + i) % self.size

    def add(self, value):
        for i in range(2):
            self.bit_array[self._hash(value, i)] = 1

    def check(self, value):
        return all(self.bit_array[self._hash(value, seed)] for seed in range(2))