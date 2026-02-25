class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        array = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in array:
                return [i, array[compliment]]
            array[nums[i]] = i
