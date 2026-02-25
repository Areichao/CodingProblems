class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        if set(target) - set(source): # if target has a letter that source does not carry, return -1
            return -1
        result = 0
        targetPointer = 0
        while targetPointer < len(target):
            