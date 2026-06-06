from collections import deque
class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.bucket = deque()
        self.total = 0
        
    def next(self, val: int) -> float:
        """ slaps in next value and computes average """
        self.bucket.append(val)
        self.total += val
        if len(self.bucket) > self.size:
            self.total -= self.bucket.popleft()
    
        return self.total / len(self.bucket)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)