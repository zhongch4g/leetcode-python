#-*-coding:utf-8 -*-
"""
    121. Best Time to Buy and Sell Stock
    Directed by user zhongch4g
    current system date 2017/4/29
"""

import sys

class Solution(object):
    def maxProfit(self, prices):

        pre = 0
        max_profit, min_profit = -sys.maxsize - 1, 0
        for i in range(1, len(prices)):
            pre += (prices[i] - prices[i-1])
            max_profit = max(max_profit, pre - min_profit)
            min_profit = min(min_profit, pre)
        if max_profit < 0:
            return 0
        return max_profit


instance = Solution()
print(instance.maxProfit([1, 6]))
