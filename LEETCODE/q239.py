import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxHeap = []
        heapq.heapify(maxHeap)
        answer = []
        # initialize the heap
        for i, val in enumerate(nums[:k]):
            heapq.heappush(maxHeap, (-val, i))
        
        # go through and find the max for each window
        p1 = 0
        p2 = k - 1
        while p2 < len(nums):
            # get "smallest" (biggest but negative) heap value
            max = maxHeap[0]
            # pop if its not in current window
            while max[1] < p1 or max[1] > p2:
                heapq.heappop(maxHeap)
                max = maxHeap[0]
            # add max to answer
            answer.append(-max[0])
            p1 += 1
            p2 += 1
            if p2 < len(nums):
                heapq.heappush(maxHeap, (-nums[p2], p2))
        # return final answer
        return answer


