#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 7:06 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 64. Minimum Path Sum.py
# @Software: IntelliJ IDEA


class Solution:
    def minPathSum(self, grid):
        if not grid or not grid[0]:
            return 0

        dp = [[0] * len(grid[0]) for i in range(len(grid))]

        # init
        for i in range(len(grid[0])):
            if i == 0:
                dp[0][i] = grid[0][i]
            else:
                dp[0][i] = grid[0][i] + dp[0][i-1]

        for j in range(1, len(grid)):
            dp[j][0] = grid[j][0] + dp[j-1][0]
        print(dp)
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        print(dp)
        return dp[-1][-1]


grid = [[1]]
solution = Solution()
solution.minPathSum(grid)
