#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/1 9:42 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 63. Unique Paths II.py
# @Software: IntelliJ IDEA


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        if m == 0:
            return 0

        n = len(obstacleGrid[0])
        if n == 0:
            return 0

        if m == 1 and n == 1:
            return 0

        dp = [[0] * n for i in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    if obstacleGrid[i][j] != 1:
                        dp[i][j] = 1
                    continue

                if i == 0:
                    if obstacleGrid[i][j] != 1:
                        dp[i][j] = dp[i][j - 1]
                    continue

                if j == 0:
                    if obstacleGrid[i][j] != 1:
                        dp[i][j] = dp[i - 1][j]
                    continue

                if obstacleGrid[i][j] == 1:
                    continue
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]