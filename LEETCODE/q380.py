import random
class RandomizedSet:
    # adding error handling for this as well

    def __init__(self):
        """ Initializes """
        # O(1) space O(2n)
        self.values = []
        self.valueIndexes = {} # key: number, value: index

    def insert(self, val: int) -> bool:
        # O(1)
        """ inserts val into set if not present, return true if item was not present, false otherwise """
        if val not in self.valueIndexes:
            self.values.append(val)
            self.valueIndexes[val] = len(self.values) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        #O(1)
        """ Removes an item val from the set if present. Returns true if the item was present, false otherwise. """
        # put value we are removing last and swap with whatever is at the end
        if val in self.valueIndexes:
            # setup variables
            index = self.valueIndexes[val] # this is the one we want to get rid of - and its current index
            lastItem = self.values[-1]
            # put last item in current index place and update hashtable
            self.values[index] = lastItem
            self.valueIndexes[lastItem] = index
            # remove last element - which is currently a dupe
            del self.valueIndexes[val]
            self.values.pop()
            return True 
        return False
        
    def getRandom(self) -> int:
        #O(n)
        """ Returns a random element from the current set of elements """
        if not self.values:
            raise ValueError("List is empty!")
        return random.choice(self.values)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()