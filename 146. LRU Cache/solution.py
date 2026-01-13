from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Move to end to show it was recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update value and move to end
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # Remove the first item (least recently used)
            self.cache.popitem(last=False)


# Test cases
if __name__ == "__main__":
    # Test case 1
    # ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    # [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    # Output: [null, null, null, 1, null, -1, null, -1, 3, 4]
    
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1) # cache is {1=1}
    lRUCache.put(2, 2) # cache is {1=1, 2=2}
    print(f"get(1): {lRUCache.get(1)} (Expected: 1)") # return 1
    lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    print(f"get(2): {lRUCache.get(2)} (Expected: -1)") # returns -1 (not found)
    lRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    print(f"get(1): {lRUCache.get(1)} (Expected: -1)") # return -1 (not found)
    print(f"get(3): {lRUCache.get(3)} (Expected: 3)") # return 3
    print(f"get(4): {lRUCache.get(4)} (Expected: 4)") # return 4
