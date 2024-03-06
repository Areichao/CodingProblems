class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        # space is 0 edge case
        if space == 0:
            return len(tasks)
        days = 0 # Keep track of number of days passed
        coolDownTracker = {} # keep track of number of days
        for task in tasks: # iterate through all tasks
            if task not in coolDownTracker: # if this is a new task
                days += 1 
                coolDownTracker[task] = space
            else: # if the task has been seen before
                # should add one here probably according to logic
                coolDownTracker[task] += 1 
                while coolDownTracker[task] != 0: # while the current task has not cooled down
                    days += 1 # add an extra day
                    for key in coolDownTracker.keys(): # reduce each day by 1
                        if coolDownTracker[key] != 0: 
                            coolDownTracker[key] -= 1
        return days



public class Solution {
    public long TaskSchedulerII(int[] tasks, int space) {     
        var dict = new Dictionary<int, long>();

        long result = 0;
        foreach (int task in tasks) {
            // add to dictionary
            if (dict.ContainsKey(task) && dict[task] > result) {
                result = dict[task] + 1;
            } else {
                result += 1;
            }

            dict[task] = result + space;
        }
        return result;
    }
}

def taskSchedulerII(self, tasks: List[int], space: int) -> int:
    dict = {}
    result = 0
    for task in tasks:
        if task in dict and dict[task] > result:
            result = dict[task] + 1
        else:
            result += 1 
        dict[task] = result + space
    return result
                    


