class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        for (index1, index2) in zip(s, t):
            if s.index(index1) != t.index(index2):
                return False
        return True
