from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.cache = OrderedDict()

    def put(self, key, value):
        if key in self.cache:
            del self.cache[key]
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value

    def get(self, key):
        if key in self.cache:
            value = self.cache[key]
            del self.cache[key]
            self.cache[key] = value
            return value
        else:
            return None


cache = LRUCache(capacity=2)

cache.put(1, 'значение1')
cache.put(2, 'значение2')
print(cache.get(1))
print(cache.get(2))
print(cache.get(3))
cache.put(3, 'значение3')
print(cache.get(1))
print(cache.get(3))
