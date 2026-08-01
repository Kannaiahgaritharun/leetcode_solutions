class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        min_price = prices[0]
        for i in range(1,len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            else:
                profit = prices[i]-min_price
                if profit > max_profit:
                    max_profit = profit
        return max_profit