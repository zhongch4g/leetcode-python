#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/26 7:00 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 221. Maximal Square.py
# @Software: IntelliJ IDEA


class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0:
            return 0

        n = len(matrix[0])
        if n == 0:
            return 0

        dp = [[0] * n for i in range(m)]
        ms = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = int(matrix[i][j])
                    ms = max(ms, dp[i][j])
                    continue

                if i > 0 and j > 0:
                    if min(dp[i-1][j], dp[i][j-1]) >= dp[i-1][j-1] and matrix[i][j] == '1':
                        dp[i][j] = dp[i-1][j-1] + 1
                    elif min(dp[i-1][j], dp[i][j-1]) < dp[i-1][j-1] and matrix[i][j] == '1':
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
                    else:
                        dp[i][j] = int(matrix[i][j])
                ms = max(ms, dp[i][j])

        return ms**2


matrix = [["0","0","0","1"],
          ["1","1","0","1"],
          ["1","1","1","1"],
          ["0","1","1","1"],
          ["0","1","1","1"]]
solution = Solution()
solution.maximalSquare(matrix)


