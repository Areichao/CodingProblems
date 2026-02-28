class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        answer = []
        i = 0
        nums.sort()
        while i < len(nums) - 2: # iterate though the whole list (index i represents the target)
            left = i + 1
            right = len(nums) - 1
            while left < right: # while the pointers havent crossed one another
                if nums[left] + nums[right] == -nums[i]: # if they cancel out to neutralize target
                    answer.append([nums[left], nums[right], nums[i]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]: # skip all duplicate numbers to prevent repeating answers
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif nums[left] + nums[right] > -nums[i]: # if its greater, iterate right down
                    right -= 1
                elif nums[left] + nums[right] < -nums[i]: # if its less, iterate left up
                    left += 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return answer