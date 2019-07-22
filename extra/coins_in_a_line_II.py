#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/20 12:22 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : coins_in_a_line_II.py
# @Software: IntelliJ IDEA


class Solution:
    """
    @param values: a vector of integers
    @return: a boolean which equals to true if the first player will win
    """
    def firstWillWin(self, values):
        dp = [0] * (len(values) + 1)
        res = self.win_or_not(values, len(values), dp, {})
        print(dp)
        return res > (sum(values)/2)

    def win_or_not(self, values, index, dp, memo):
        if index in memo.keys():
            return memo[index]
        if index ==0:
            return 0
        elif index == 1:
            dp[index] = values[len(values) - index]
            return dp[index]
        elif index == 2:
            dp[index] = values[len(values) - index] + values[len(values) - index + 1]
            return dp[index]
        elif index == 3:
            dp[index] = values[len(values) - index] + values[len(values) - index + 1]
            return dp[index]
        else:
            dp[index] = max(
                min(self.win_or_not(values, index - 2, dp, memo), self.win_or_not(values, index - 3, dp, memo)) + values[len(values)-index],
                min(self.win_or_not(values, index - 3, dp, memo), self.win_or_not(values, index - 4, dp, memo)) + values[len(values)-index] + values[len(values)-index+1]
            )
        memo[index] = dp[index]
        return dp[index]


solution = Solution()
res = solution.firstWillWin([16,27,25,23,25,16,12,9,1,2,7,20,19,23,16,0,6,22,16,11,8,27,9,2,20,2,13,7,25,29,12,12,18,29,27,13,16,1,22,9,3,21,29,14,7,8,14,5,0,23,16,1,20])
print(res)