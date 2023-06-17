import collections
class MyQueue:

    def __init__(self):
        self.stack1 = collections.deque([])
        self.stack2 = collections.deque([])

    def push(self, x: int) -> None:
        """ pushes element x to the back of the queue """
        self.stack1.append(x)

    def pop(self) -> int:
        """ pop first element in FIFO queue """
        if self.empty(): # if theres nothing to pop
            return None
        if len(self.stack2) > 0: # if stack 2 is filled, pop from that
            return (self.stack2.pop())
        while len(self.stack1) > 0: # pop from stack 1 and append onto stack two
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
    def peek(self) -> int:
        """ look at first element in FIFO queue"""
        if self.empty():
            return None
        if len(self.stack2) > 0:
            return (self.stack2[-1])
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())
        return self.stack2[-1]
    def empty(self) -> bool:
        return (len(self.stack1) == 0 and len(self.stack2) == 0)



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()