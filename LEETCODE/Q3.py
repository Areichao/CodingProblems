class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        leftPointer = 0
        char_dupes = {}
        result = 0
        for rightPointer in range(len(s)):
            # if we find a dupe, update new left pointer
            if s[rightPointer] in char_dupes and char_dupes[s[rightPointer]] >= leftPointer:
                leftPointer = char_dupes[s[rightPointer]] + 1
            # update current maximum and new most recent index
            result = max(result, rightPointer - leftPointer + 1)
            char_dupes[s[rightPointer]] = rightPointer
        return result
        # time complexity O(n)
        # space complexity O(mins(m,n))


            
            
