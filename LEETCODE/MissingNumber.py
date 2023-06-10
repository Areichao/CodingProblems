class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        result = len(nums)
        for num in range(len(nums)):
            result += (num - nums[num])
        return result