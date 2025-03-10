from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    # get the value of the key if it exists in the cache, otherwise return None
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # if key is there we will move it to the end of the list and get the value
        self.cache.move_to_end(key)
        return self.cache[key]

    # set the value of the key in the cache
    def set(self, key: int, value: int) -> None:
        if key in self.cache:
            # if key is there we will move it to the end of the list
            self.cache.move_to_end(key)
        self.cache[key] = value

        # if the cache is full we will remove the first key
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


# Example Usage
lru = LRUCache(3)
lru.set(1, 10)
lru.set(2, 20)
lru.set(3, 30)
print(lru.get(1))  # 10 (Cache hit)
lru.set(4, 40)     # Evicts key 2 (least recently used)
print(lru.get(2))  # -1 (Cache miss)
print(lru.get(3))  # 30 (Cache hit)