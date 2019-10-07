#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/6 6:07 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 123. Best Time to Buy and Sell Stock III.py
# @Software: IntelliJ IDEA



import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        1.status
        f[i][j] the first i prices maximum profit in j stage
        we have 5 stage
        stage1 haven't buy any stock
        stage2 already buy stock but haven't sell
        stage3 already sell stock first buy
        stage4 already buy stock second time
        stage5 already sell stock second buy

        2.function
        for stage 1, 3, 5
        f[i][j] = max j  = 1, 3, 5 (f[i - 1][j], f[i - 1][j - 1] + P[i - 1] - P[i - 2])
        for stage 2, 4
        f[i][j] = max j = 2, 4 (f[i - 1][j - 1], f[i - 1][j] + P[i - 1] - P[i - 2])

        3.initial
        n = len(prices)
        f[n + 1][5 + 1] stage start at 1
        f[0][1] = 0
        f[0][2] = f[0][3] = f[0][4] = f[0][5] = - sys.maxsize - 1

        4.calculation order
        top dowm - left right
        """
        if not prices:
            return 0
        n = len(prices)

        # dp[n + 1][5 + 1]
        dp = [[-sys.maxsize - 1] * 6 for i in range(n + 1)]
        dp[0][1] = 0

        for i in range(1, n + 1):

            for j in range(1, 6, 2):
                dp[i][j] = dp[i - 1][j]
                if i - 2 >= 0 and j - 1 >= 0 and dp[i - 1][j - 1] != - sys.maxsize - 1:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + prices[i - 1] - prices[i - 2])

            for j in range(2, 6, 2):
                dp[i][j] = dp[i - 1][j - 1]
                if i - 2 >= 0 and j - 1 >= 1 and dp[i - 1][j] != - sys.maxsize - 1:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j] + prices[i - 1] - prices[i - 2])

        return max(dp[n][1], dp[n][3], dp[n][5])


