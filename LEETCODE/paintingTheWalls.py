class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        @cache
        def dp(i, remain):
            if remain <= 0:
                # if there are no walls remaining, return 0
                return 0
            elif i == n:
                # if we reached the maximum number of walls, return infinite
                return float('inf')
            
            # if the wall i is gonna be painted or not
            # if it is painted, add the cost + remaining walls (-1 for the wall currently painted and - time[i] for time for free painter)
            paint = cost[i] + dp(i + 1, remain - time[i] - 1)
            # do nothing, iterate foward
            dontPaint = dp(i + 1, remain)
            return min(paint, dontPaint)
        
        n = len(cost)
        # start at index 0, n is maximum number of walls (remain)
        return dp(0, n)