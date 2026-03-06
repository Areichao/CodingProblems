class Solution:
    def findMin(self, nums: List[int]) -> int:
        # check if nums isnt rotated, if its not, just return first element. or only one element
        if len(nums) == 1 or nums[0] < nums[-1]:
            return nums[0]
        # otherwise, do an altered version of binary search
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = (right + left) // 2
            # if middle is greater than right and we are out of order, that means smallest is somewhere on the right
            if nums[middle] > nums[right]:
                left = middle + 1
            else: # otherwise, that means the starting point is somewhere between left and middle
                right = middle
        return nums[right]