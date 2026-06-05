from collections import deque
class HitCounter:

    def __init__(self):
        # O(n) where n is number of unique time stamps (space)
        self.hits = deque()
        self.total = 0
        
    def hit(self, timestamp: int) -> None:
        """ insert hit into timestamp """
        # O(1) time
        # store as like (time, count). if its the last value, just add
        # error handling for practice
        if not isinstance(timestamp, int):
            raise TypeError("Timestamp must be an integer in seconds")
        elif timestamp < 0:
            raise ValueError("Timestamp must be a non negative integer")
        elif self.hits and timestamp < self.hits[-1][0]:
            raise ValueError("Timestamp must be greater or equal to last asserted time")
        if self.hits and self.hits[-1][0] == timestamp:
            self.hits[-1][1] += 1
        else:
            self.hits.append([timestamp, 1])
        self.total += 1
        
    def getHits(self, timestamp: int) -> int:
        # O(n) worst case where every value is outdated
        """ get number of hits within 5 mins of timestamp """
        while self.hits and self.hits[0][0] <= timestamp - 300:
            self.total -= self.hits[0][1]
            self.hits.popleft()
        return self.total


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)