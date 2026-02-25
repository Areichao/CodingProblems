class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0 for _ in range(len(temperatures))]
        stack = [] # will always have a order of hottest to coldest temp going left to right
        for i in range(len(temperatures)):
            if not stack or temperatures[i] <= temperatures[stack[-1]]:
                stack.append(i) # save the index to calculate number of days.
            else:
                while stack and temperatures[i] > temperatures[stack[-1]]: # while temp is greater than 
                    pop = stack.pop()
                    answer[pop] = i - pop
                stack.append(i) # take out while temp is hotter, then place itself as next smallest temp
        return answer