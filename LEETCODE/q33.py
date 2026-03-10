class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            # basic cases to return the value
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            elif nums[middle] == target:
                return middle
            # search part 
            # check if left side is sorted and target is between
            elif nums[left] <= nums[middle] and nums[left] < target < nums[middle]:
                right = middle - 1
            # else, if the left isnt it but right is sorted and target in between
            elif nums[middle] <= nums[right] and nums[middle] < target < nums[right]:
                left = middle + 1
            # else, if the right is sorted but it wasnt in the right side
            elif nums[middle] <= nums[right]:
                right = middle - 1
            # otherwise, if left is sorted but it wasnt in the left side
            else:
                left = middle + 1
        return -1