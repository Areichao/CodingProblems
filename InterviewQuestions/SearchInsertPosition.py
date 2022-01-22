import math
class Solution(object):
    def searchInsert(self, nums, target, index = 0):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        middleIndex = len(nums)//2
        index += middleIndex
        # base case
        if (len(nums) == 0):
            return 0
        elif ((len(nums) == 1) and nums[middleIndex] != target):
            if nums[middleIndex] < target:
                return index + 1
            return index
        # other base case
        elif nums[middleIndex] == target:
            return index
        #recursive case
        if nums[middleIndex] > target:
            index -= middleIndex
            return self.searchInsert(nums[:middleIndex], target, index)
        elif nums[middleIndex] < target:
            return self.searchInsert(nums[middleIndex:], target, index)
            
# Testing code asda
example = Solution()
print(example.searchInsert([1,3,5,6], 2))