class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """ return maximum profit """
        # initialize the profit and left pointer
        profit = p1 = 0
        # iterate through the stock prices
        for i in range(1, len(prices)):
            # if value is less than that in p1, set p1 to this new pointer
            if prices[i] < prices[p1]:
                p1 = i
            # check profit otherwise
            else:
                profit = max(profit, prices[i] - prices[p1])
        return profit  