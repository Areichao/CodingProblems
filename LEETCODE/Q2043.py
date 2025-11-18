class Bank:

    # Time: O(1) space O(n)
    def __init__(self, balance: List[int]):
        self.balance = balance

    # Time: O(1) space O(1)
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self._check_valid_account(account1) and self._check_valid_account(account2):
            if self._check_account_balance(account1) >= money:
                self.balance[account1 - 1] -= money
                self.balance[account2 - 1] += money
                return True
        return False

    # Time: O(1) space O(1)
    def deposit(self, account: int, money: int) -> bool:
        if self._check_valid_account(account):
            self.balance[account - 1] += money
            return True
        return False

    # Time: O(1) space O(1)
    def withdraw(self, account: int, money: int) -> bool:
        if self._check_valid_account(account):
            if self._check_account_balance(account) >= money:
                self.balance[account - 1] -= money
                return True
        return False

    # Time: O(1) Space O(1)
    def _check_valid_account(self, account: int) -> bool:
        """ returns true if account is a number between 1 and n """
        return account >= 1 and account <= len(self.balance)
    
    # Time O(1) Space O(1)
    def _check_account_balance(self, account: int) -> int:
        """ returns the balance of an account """
        return self.balance[account - 1]
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)