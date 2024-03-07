# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # empty time slot list
        times = []
        # take the inside time slots and add it into a list (doesnt really matter whos time slot is whose)
        for employee in schedule:
            for timeSlot in employee:
                times.append(timeSlot)
        # sort by start time (TIMSORT -> O(nlogn) time complexity)
        times.sort(key = lambda s: s.start)
        merged = []
        # merge time slots
        for time in times:
            # if merged is empty or time is greater than the previous end add it into merged
            if not merged or time.start > merged[-1].end:
                merged.append(time)
            else: # if start time is earlier than previous end, set new end to be larger value
                merged[-1].end = max(merged[-1].end, time.end)
        # finally, find free times
        free = []
        for time1, time2 in zip(merged, merged[1:]):
            free.append(Interval(start = time1.end, end = time2.start))
        return free

Andrew = Solution()
Andrew.employeeFreeTime([[[1,2],[5,6]],[[1,3]],[[4,10]]])




