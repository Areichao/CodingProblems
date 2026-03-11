class TimeMap:

    def __init__(self):
        self.times = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.times:
            self.times[key].append((timestamp, value))
        else:
            self.times[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        # if no such key, or the first timestamp is greater than the one we are trying to retrieve
        if key not in self.times or self.times[key][0][0] > timestamp:
            return ""
        # otherwise, perform binary search
        result = ""
        left = 0
        right = len(self.times[key]) - 1
        while left <= right:
            middle = (left + right) // 2
            if self.times[key][middle][0] <= timestamp:
                # there could be more on the right of list, 
                left = middle + 1
                result = self.times[key][middle][1]
            else:
                right = middle - 1
        return result 
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)