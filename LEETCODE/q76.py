class Solution:
    def _valid_window(self, d1: dict, d2: dict) -> bool:
        """ returns true if d1 has equal or more numbers of same characters"""
        for c in d1:
            if d1[c] < d2[c]:
                return False
        return True
        
    def minWindow(self, s: str, t: str) -> str:
        # not possible if t is longer than s
        if len(t) > len(s):
            return ""
        # update frequencies for t, set the same value to 0 in s.
        t_freq = {}
        s_freq = {}
        for letter in t:
            if letter in t_freq:
                t_freq[letter] += 1
            else:
                t_freq[letter] = 1
                s_freq[letter] = 0
        # iterate through s, with left and right pointer.
        left = 0
        answer = ""

        for right in range(len(s)):
            # add value into current windows freq
            if s[right] in s_freq:
                s_freq[s[right]] += 1
            # check for valid window
            while self._valid_window(s_freq, t_freq):
                # get substring
                curr = s[left:right+1]
                # if its suitable for the new answer update, update it
                if not answer or len(curr) < len(answer):
                    answer = curr
                # iterate left as long as it has a valid window. max left value will be right + 1
                if s[left] in s_freq:
                    s_freq[s[left]] -= 1
                left += 1
        return answer

