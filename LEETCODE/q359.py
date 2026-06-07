class Logger:

    def __init__(self):
        """ initialize a dictionary to hold all messages """
        self.messages = {}
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """ returns true if message was not printed within the last 10 seconds """
        if message not in self.messages or self.messages[message] <= timestamp - 10:
            self.messages[message] = timestamp
            return True
        return False
        

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)