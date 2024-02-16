class Solution(object):
    def maxSumArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumMax = nums[0]
        currentSum = 0

        for number in nums:
            if currentSum < 0:
                currentSum = 0
            currentSum += number
            sumMax = max(sumMax, currentSum)
        return sumMax

# TESTING CODE HERE
example1 = Solution()
print(example1.maxSumArray([-2,1,-3,4,-1,2,1,-5,4]))


# 2024 version
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = currentValue = nums[0]
        for num in nums[1:]: # start with the second number
            if num >= currentValue + num: # if the current number is greater than current sublist 
                currentValue = num 
            else:
                currentValue = currentValue + num
            if currentValue > maximum: # if the new sublist is greater than the maximum value
                maximum = currentValue
        return maximum
    
# simplified editorial version using max function
    
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = currentValue = nums[0]
        for num in nums[1:]: # start with the second number
            currentValue = max(num, currentValue + num)
            maximum = max(currentValue, maximum)
        return maximum