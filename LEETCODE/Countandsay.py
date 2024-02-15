import re

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: # base case
            return "1"
        
        # new value
        new = "" 
        # get different number splits from previous recursion
        splits = self.split_by_character(self.countAndSay(n-1)) 
        for num in splits: # iterate different splits
            new += str(len(num)) + num[0] # concatinate number of numbers + the number itself
        return new

    def split_by_character(self, string):
        return [match.group(0) for match in re.finditer(r'((.)\2*)', string)]
        