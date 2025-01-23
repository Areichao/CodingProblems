class Solution:
    def longestPalindrome(self, s: str) -> int:
        letters: dict[str:int] = {} # initialize a letter:count dictionary
        oddTracker: int = 0 # minimum
        palindromeSize: int = 0 # initialize
        for letter in s:
            if letter not in letters:
                letters[letter] = 1 # initialize count
                oddTracker += 1 # add that there is one odd number
            else: # letter is already inside dictionary
                letters[letter] += 1
                # if even, add 2 to palindrome size (and -1 from oddtracker). if odd, add 1 to odd tracker.
                if letters[letter] % 2 == 0:
                    palindromeSize += 2
                    oddTracker -= 1
                else:
                    oddTracker += 1
        # check if there is an odd number of letters
        if oddTracker > 0:
            palindromeSize += 1
        return palindromeSize
