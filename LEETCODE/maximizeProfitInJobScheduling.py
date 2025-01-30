# class Solution:
#     def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
#         @cache
#         def dp(i, end):
#             if i >= end:
#                 return 0
#             # algorithm for taking
#             # if we take a job, we need to update the index to match the next start which contains the same number or larger
#             indexCurr = i
#             for j in startTime[i:]:
#                 indexCurr += 1
#                 if j >= endTime[i]:
#                     break
#             take = profit[i] + dp(indexCurr, end)
#             dontTake = dp(i+1, end)
#             return max(take, dontTake)
#         n = len(startTime)
#         return dp(0, n)

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # combine start time, end time and profit into one tuple
        jobs = [[startTime[i], endTime[i], profit[i]] for i in range(len(startTime))]
        
        # now sort the jobs based on their start times
        jobs.sort(key=lambda x: x[0])

        # function to search for next available job (binary search)
        def nextAvailable(lastEnd):
            start = 0
            end = len(startTime) - 1
            final = len(startTime)

            while start <= end:
                middle = (start + end) // 2 # floor division
                if jobs[middle][0] >= lastEnd:
                    final = middle
                    end = middle - 1
                else:
                    start = middle + 1
            return final 
        

        # use memoization to maximize profit
        @cache
        def dp(i):
            # base case -> we reached the end (no more jobs)
            if i >= len(startTime):
                return 0
            
            # option 1 -> skip current job
            notTake = dp(i+1)

            # option 2 -> take the job
            # need to add profit + next dp value with next index
            nextIndex = nextAvailable(jobs[i][1])
            take = jobs[i][2] + dp(nextIndex)
            return max(notTake, take)
        
        return dp(0)