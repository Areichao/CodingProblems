class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # we can use dp for this, however its probably not the best option
        # use double pointers
        if len(s) == 0:
            return True
        ps = 0
        for letter in t:
            if letter == s[ps]:
                ps += 1
                if ps == len(s): return True
        return False