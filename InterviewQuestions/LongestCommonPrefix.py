# Original slow solution 
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs[0] == "":
            return ""
        for sub in range(1, len(strs[0])+1):
            previousValue = strs[0][0:sub-1]
            currSubstring = strs[0][0:sub]
            for word in strs:
                if (word[:sub] != currSubstring) and (sub == 1):
                    return ""
                elif (word[:sub] != currSubstring):
                    return previousValue 
        return currSubstring

# code testing 
example1 = Solution()
print(example1.longestCommonPrefix(["ab", "a"]))


