class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        startEnd = [float('inf'), float('-inf')] # keep track of lowest start and highest end
        # go through each element
        for interval in intervals:
            # sort them by start time
            # if next start time is earlier than end time then it doesnt work
