class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # T: O(n) space: O(m) (m = number of elements minus all duplicates)
        left = 0
        dupes = {}
        longest = 0
        for right in range(len(s)):
            # if dupe, move left pointer up
            if s[right] in dupes and dupes[s[right]] >= left:
                left = dupes[s[right]] + 1

            # otherwise, add or update dupes with new location, and update longest
            longest = max(longest, right - left + 1)
            dupes[s[right]] = right
        return longest


            
            
