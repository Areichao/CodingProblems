class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums) # convert into set for O(1) lookup and bc we dont care about dupes
        longest = 0
        for num in numset:
            if num - 1 not in numset: # if this is not already apart of a long sequence (not the first number in sequence)
                currLongest = 1
                i = 1
                while num + i in numset:
                    currLongest += 1
                    i += 1
                if currLongest > longest:
                    longest = currLongest
        return longest