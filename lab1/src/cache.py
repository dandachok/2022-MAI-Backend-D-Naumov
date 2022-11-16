from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int = 10):
        self.capacity = capacity
        self.values = OrderedDict()

    def get(self, key: str) -> str:
        if key not in self.values:
            return ''
        else:
            self.values[key] = self.values.pop(key)
            return self.values[key]

    def set(self, key: str, value: str) -> None:
        if key not in self.values:
            if len(self.values) == self.capacity:
                self.values.popitem(last=False)
        else:
            self.values.pop(key)
        self.values[key] = value

    def rem(self, key: str) -> None:
        self.values.pop(key)