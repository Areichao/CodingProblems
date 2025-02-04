from collections import defaultdict
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:
        """ splitwise simplified debts algorithm ??? i think """
        # calculate how much debt or surplus each person has by iterating through the transactions list
        # hardest part is determining the least amount of transactions
        # maximum of n (where n is number of people in debt) transactions
        personalDebts = defaultdict(int)
        for sender, receiver, amount in transactions:
            personalDebts[sender] -= amount
            personalDebts[receiver] += amount

            # recurively backtrack here
            # get list of negatives and positives, ultimately we dont care who sent or recieved anything
            def recursive(negatives, positives):
                pass
                # infinite counter, at the end compare counter and recursion and see which value is smaller
                # finish this another day