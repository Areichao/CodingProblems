import collections 
import itertools
class TodoList:

    def __init__(self):
        """ initialize the to do list """
        self.taskId = itertools.count(1) # count starts at 1
        self.tasks = collections.defaultdict(dict) # userId : {taskId: [description, duedate, set(tags)]}
        
    def addTask(self, userId: int, taskDescription: str, dueDate: int, tags: List[str]) -> int:
        """ adds task to userId, with description and due date and tags """
        taskId = next(self.taskId)
        self.tasks[userId][taskId] = [taskDescription, dueDate, set(tags)]
        return taskId
        
    def getAllTasks(self, userId: int) -> List[str]:
        """ returns list of all tasks not completed ordered by due date """
        
        tasks = list(self.tasks[userId].values())
        tasks.sort(key=lambda x: x[1]) # sort by the duedate
        return [desc for desc, _, _ in tasks]
        

    def getTasksForTag(self, userId: int, tag: str) -> List[str]:
        """ returns a list of tasks with tag that are not complete, ordered by due date """

        tasks = list(self.tasks[userId].values())
        tasks.sort(key=lambda x: x[1]) # sort by the duedate
        return [desc for desc, _, tags in tasks if tag in tags]

    def completeTask(self, userId: int, taskId: int) -> None:
        """ marks task as complete (deleted from to do list)"""
        
        if taskId in self.tasks[userId]:
            del self.tasks[userId][taskId]
        

# Your TodoList object will be instantiated and called as such:
# obj = TodoList()
# param_1 = obj.addTask(userId,taskDescription,dueDate,tags)
# param_2 = obj.getAllTasks(userId)
# param_3 = obj.getTasksForTag(userId,tag)
# obj.completeTask(userId,taskId)