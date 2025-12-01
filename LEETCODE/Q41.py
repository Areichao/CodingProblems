class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        lenNums = len(nums)
        for i in range(lenNums):
            # keep swapping this value until we get whatever we want
            while (nums[i] > 0 and nums[i] <= lenNums) and nums[nums[i] - 1] != nums[i]:
                # swap values
                # can use nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1] which makes it slightly slower but better for space
                # dont do the swap the other way (like nums[i] first) cuz it wont work

                oldVal = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = oldVal
        # go through sorted nums, keep track of lowest positive integer
        for i in range(lenNums):
            # if its a valid number
            if nums[i] != i + 1:
                return i + 1
        return lenNums + 1 

