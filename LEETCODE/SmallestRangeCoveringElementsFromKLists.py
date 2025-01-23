import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        maximum = float('-inf')
        pq = []
        for i in range(len(nums)):
            maximum = max(maximum, nums[i][0])
            # store (value, row, index)
            heapq.heappush(pq, (nums[i][0], i, 0))
        
        # current answer is smallest value and biggest in all the smallest ones
        answer = [pq[0][0], maximum]
        while True:
            _, row, index = heapq.heappop(pq)
            # if we hit an end point, break the loop
            if index == len(nums[row]) - 1:
                break
            maximum = max(maximum, nums[row][index+1])
            heapq.heappush(pq, (nums[row][index+1], row, index+1))
            # if were seeing a value that is strictly less than our current range
            if maximum - pq[0][0] < answer[1] - answer[0]:
                answer = [pq[0][0], maximum]
            

        return answer
