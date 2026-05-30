class MyHashMap:
    def __init__(self):
        """ init """
        # O(2069)
        self.size = 2069
        self.buckets = [[] for _ in range(2069)]

    def _getBucket(self, key: int) -> int:
        """ given the key, returns which bucket it belongs in """
        # O(1)
        if not isinstance(key, int):
            raise TypeError("key must be an integer")
        return key % 2069
    
    def put(self, key: int, value: int) -> None:
        """ inserts key and value into hashmap or update if exists """
        # error handling
        if not isinstance(key, int) or not isinstance(value, int):
            raise TypeError("inputs must be integers")
        # O(1) but if everything is in the same fuckibng bucket then O(n)
        bucket = self._getBucket(key)
        # check the current bucket to see if this key exists. if it is, replace the value with new value
        for pair in self.buckets[bucket]:
            if pair[0] == key:
                pair[1] = value
                return 
        # if not, just append into this bucket
        self.buckets[bucket].append([key, value])

    def get(self, key: int) -> int:
        """ return value which key is mapped to or -1 """
        # O(1) but if everything is in the same fuckibng bucket then O(n)
        if not isinstance(key, int):
            raise TypeError("key must be an integer")
        bucket = self._getBucket(key)
        # go through bucket to see if it exists
        for pair in self.buckets[bucket]:
            if pair[0] == key:
                return pair[1]
        return -1 

    def remove(self, key: int) -> None:
        """ remove key and value if map contains key """
        # O(1) but if everything is in the same fuckibng bucket then O(n)
        if not isinstance(key, int):
            raise TypeError("key must be an integer")
        bucket = self._getBucket(key) 
        # go through bucket to see if key exists, and delete if it does
        for i in range(len(self.buckets[bucket])):
            if self.buckets[bucket][i][0] == key:
                del self.buckets[bucket][i]
                return
