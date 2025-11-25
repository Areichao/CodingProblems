class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        lenNums = len(nums)
        for i in range(lenNums):
            # keep swapping this value until we get whatever we want
            while (nums[i] > 0 and nums[i] <= lenNums) and i + 1 != nums[i] and nums[nums[i] - 1] != nums[i]:
                # swap values
                oldVal = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = oldVal
        # go through sorted nums, keep track of lowest positive integer
        for i in range(lenNums):
            # if its a valid number
            if nums[i] != i + 1:
                return i + 1
        return lenNums + 1 



