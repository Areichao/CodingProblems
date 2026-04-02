import collections
class LRUCache:

    def __init__(self, capacity: int):
        
        self.capacity = capacity
        self.dict = collections.OrderedDict()

    def get(self, key: int) -> int:
        if key in self.dict:
            # if we were to do this the doubly linked list way
            # 1. update doubly linked list, put key at the end
            # 2. update address of key inside the hashtable
            # 3. return just the value
            self.dict.move_to_end(key)
            return self.dict[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            # again if we were to do this doubly linked list way
            # 1. update doubly linked list, put key at the end
            # 2. update address of key inside hashtable along with the value
            self.dict.move_to_end(key)
            self.dict[key] = value
        else:
            # doubly linked list method: 
            # 1. if capacity is > 0, add the key into the cache & address to end of doubly linked list
            # 2. update doubly linked list to have this key at the tail
            # 3. subtract one from capacity
            self.dict[key] = value

            if self.capacity > 0:
                self.capacity -= 1
            # 1. otherwise, if capacity is at 0, delete head of doubly linked list from hash table
            # 2. then delete it from the doubly linked list itself
            else:
                self.dict.popitem(False)
            # final: now in both cases, we will add the value to the hash table & end of doubly linked list
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)