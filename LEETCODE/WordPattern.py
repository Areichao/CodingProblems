class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern) != len(s.split()):
            return False
        s = s.split()
        dict = {}
        dict2 = {}
        for i in range(len(pattern)):
            if pattern[i] not in dict:
                dict[pattern[i]] = s[i]
            else:
                if dict[pattern[i]] != s[i]:
                    return False
            if s[i] not in dict2:
                dict2[s[i]] = pattern[i]
            else:
                if dict2[s[i]] != pattern[i]:
                    return False
        return True