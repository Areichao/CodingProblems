class ATM:

    def __init__(self):
        """ initializes the number of bank notes in the ATM """
        # space of O(1) basically
        self.bills = ([0, 20], [0, 50], [0, 100], [0, 200], [0, 500]) # [num bills, worth]
        

    def deposit(self, banknotesCount: List[int]) -> None:
        """ deposit bank notes into the ATM """
        # O(1)
        for i in range(5):
            self.bills[i][0] += banknotesCount[i]
        

    def withdraw(self, amount: int) -> List[int]:
        """ Withdraw, or return [-1] if not possible """
        # space O(1), time O(1)
        answer = [0 for _ in range(5)] # keep track of possible number of bills we will withdraw
        for i in range(4, -1, -1): #(start, stop, step) -> 4 to 0
            # while there is 1 or more of this bill, and amount > bill amount
            count, value = self.bills[i]
            take = min(count, amount // value)
            amount -= take * value
            answer[i] = take
        
        # otherwise, subtract it from our ATM then return our answer
        if not amount:
            for i in range(5):
                self.bills[i][0] -= answer[i]
        # return the answer
        return [-1] if amount else answer
            




        


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)