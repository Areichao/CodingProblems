class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        longest = 0
        chars = {}
        freq = 0
        for right in range(len(s)):
            # check if window is still valid at this point
            size = right - left + 1
            # update frequency of the letter or add into hash table
            if s[right] in chars:
                chars[s[right]] += 1
            else:
                chars[s[right]] = 1
            # if the current frequency for this window is greater, update freq
            freq = max(freq, chars[s[right]])
            # if not valid, move left until it is valid
            while size - freq > k:
                # decrement left value by one
                chars[s[left]] -= 1
                left += 1
                size = right - left + 1 

            # update longest
            longest = max(longest, size)
        return longest