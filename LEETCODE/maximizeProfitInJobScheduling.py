class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        @__cached__
        def dp(i, end):
            if i >= end:
                return 0
            # algorithm for taking
            # if we take a job, we need to update the index to match the next start which contains the same number or larger
            indexCurr = i
            for j in startTime[i:]:
                indexCurr += 1
                if j >= endTime[i]:
                    break
            take = profit[i] + dp(indexCurr, end)
            dontTake = dp(i+1, end)
            return max(take, dontTake)
        n = len(startTime)
        return dp(0, n)