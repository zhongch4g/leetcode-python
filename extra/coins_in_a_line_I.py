#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/19 4:56 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : coins_in_a_line_I.py
# @Software: IntelliJ IDEA


class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def firstWillWin(self, n):
        dp = [0] * (n + 1)
        memo = {}
        res = self.win_or_not(n, dp, memo)
        print(memo, res)
        return res

    def win_or_not(self, n, dp, memo):
        if n in memo.keys():
            return dp[n]
        if n == 0:
            dp[n] = False
            return dp[n]
        elif n == 1 or n == 2:
            dp[n] = True
            return dp[n]
        elif n == 3:
            dp[n] = False
            return dp[n]
        else:
            dp[n] = (self.win_or_not(n-2, dp, memo) and self.win_or_not(n-3, dp, memo)) or \
                    (self.win_or_not(n-3, dp, memo) and self.win_or_not(n-4, dp, memo))
        memo[n] = dp[n]
        # Be attention return value
        return dp[n]

solution = Solution()
res = solution.firstWillWin(11)
print(res)
