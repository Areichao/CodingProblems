import collections
class LFUCache:

    def __init__(self, capacity: int):
        """ initialization """
        # capacity init
        self.capacity = capacity
        self.minFreq = 0

        # containers
        self.cache = {} # key: value
        self.key2freq = {} # key: use counter
        self.counterBuckets = collections.defaultdict(collections.OrderedDict) # use counter: ordered set of keys (easy delete, retains order)
        

    def get(self, key: int) -> int:
        """ gets the key and returns value or -1 if it doesnt exist """
        value = self.cache.get(key, -1)
        # if we have a value, update frequency and move it to different bucket
        if value != -1:
            self._updateBucket(key)
        return value
        

    def put(self, key: int, value: int) -> None:
        """ insert or update key. if capacity is reached, deletes LFU """
        # if its already in cache, just update everything including frequency
        if key in self.cache:
            self.cache[key] = value
            self._updateBucket(key)
            return 

        # if capacity is reached, remove from all containers
        if len(self.cache) == self.capacity:
            # get key of LFU, and least recently used key
            leastRecent = next(iter(self.counterBuckets[self.minFreq]))
            # remove key from all containers
            del self.cache[leastRecent]
            del self.key2freq[leastRecent]
            del self.counterBuckets[self.minFreq][leastRecent]
            if not self.counterBuckets[self.minFreq]:
                del self.counterBuckets[self.minFreq]

        # initialize counter and add to a counter bucket if key is not in cache. make minFreq one
        self.key2freq[key] = 1
        self.counterBuckets[1][key] = None
        self.minFreq = 1
        # add key into cache
        self.cache[key] = value

    def _updateBucket(self, key: int) -> None:
        """ removes from old bucket and put it in a new use counter bucket """
        useCounter = self.key2freq[key]
        del self.counterBuckets[useCounter][key] 
        self.key2freq[key] += 1
        self.counterBuckets[useCounter + 1][key] = None
        # if old bucket is empty, and min freq was equal to the old bucket count, update
        if not self.counterBuckets[useCounter]:
            del self.counterBuckets[useCounter]
            if self.minFreq == useCounter:
                self.minFreq += 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)