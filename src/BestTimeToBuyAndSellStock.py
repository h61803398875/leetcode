# -*- coding:utf8 -*-

class Solution(object):
    """Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.
    """

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1:
            return 0

        max_profit = 0
        min_price = prices[0]

        for price in prices[1:]:
            profit = price - min_price
            max_profit = max_profit if profit <= max_profit else profit
            if min_price > price:
                min_price = price

        return max_profit
