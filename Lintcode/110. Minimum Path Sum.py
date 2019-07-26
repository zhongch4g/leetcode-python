#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/24 9:47 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 110. Minimum Path Sum.py
# @Software: IntelliJ IDEA

import sys
class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        if m == 0:
            return 0
        if n == 0:
            return 0

        dp = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]

                t = sys.maxsize
                if i > 0:
                    t = min(t, dp[i-1][j])
                if j > 0:
                    t = min(t, dp[i][j-1])
                dp[i][j] = t + grid[i][j]
        return dp[m-1][n-1]

