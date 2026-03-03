class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = (right + left) // 2
            if target == nums[middle]: 
                return middle
            elif target > nums[middle]:
                left = middle + 1
            else:
                right = middle
        if left < len(nums) and nums[left] == target:
            return left
        else:
            return -1