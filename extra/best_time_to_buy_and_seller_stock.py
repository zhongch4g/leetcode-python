#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/3 10:33 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : best_time_to_buy_and_seller_stock.py
# @Software: IntelliJ IDEA

import sys
class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        profit = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
        min_range, max_range = 0, -sys.maxsize
        prefix = 0

        for pro in profit:
            prefix += pro
            max_range = max(max_range, prefix - min_range)
            min_range = min(prefix, min_range)
        if max_range < 0:
            return 0
        return max_range

solution = Solution()
result = solution.maxProfit([3,2,3,1,2])
print(result)
