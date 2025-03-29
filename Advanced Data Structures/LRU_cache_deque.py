from collections import deque

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.order = deque()
        self.cache = {}

    # get the value of the key if it exists in the cache, otherwise return -1
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # if key is there we will move it to the end of the deque and get the value
        self.order.remove(key)
        self.order.append(key)
        return self.cache[key]

    # set the value of the key in the cache
    def set(self, key: int, value: int) -> None:
        if key in self.cache:
            # if key is there we will move it to the end of the deque
            self.order.remove(key)
            self.order.append(key)
        self.cache[key] = value

        # if the cache is full we will remove the first key
        if len(self.cache) > self.capacity:
            lru_key =self.order.popleft()
            del self.cache[lru_key]