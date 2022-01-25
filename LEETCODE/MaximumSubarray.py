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