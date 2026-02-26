class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 2 pointer, go till pointers cross one another
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum(): # if left or right is not A-Z a-z then skip that one
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left].lower() != s[right].lower(): # in the case that they are both lowercase letters but not the same, return False
                return False
            else: # otherwise iterate both and check the next letter
                left += 1
                right -= 1
        # if the pointers are equal or cross we have a palindrome
        return True
