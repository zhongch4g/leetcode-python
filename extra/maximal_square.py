#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/14 4:02 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : maximal_square.py
# @Software: IntelliJ IDEA


"""
Given a 2D binary matrix filled with 0's and 1's,
find the largest square containing all 1's and return its area.
"""


class Solution:
    """
    @param matrix: a matrix of 0 and 1
    @return: an integer
    """
    def maxSquare(self, matrix):
        # Initialization
        dp = [[-1]*len(matrix[0]) for i in range(len(matrix))]
        max_space = -1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i > 0:
                    if j > 0:
                        if matrix[i][j] == 1:
                            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
                        else:
                            dp[i][j] = 0
                    else:
                        dp[i][j] = matrix[i][j]
                else:
                    dp[i][j] = matrix[i][j]
                max_space = dp[i][j] if dp[i][j] > max_space else max_space
        return max_space **2

    def maxSquare_reduce_spcace(self, matrix):
        # Initialization
        dp = [[-1]*len(matrix[0]) for i in range(2)]
        max_space = -1
        for i in range(len(matrix)):
            dp[i%2][0] = matrix[i][0]
            max_space = min(dp[i%2][0], max_space)
            for j in range(1, len(matrix[0])):
                if i > 0:
                    if matrix[i][j] == 1:
                        dp[i%2][j] = min(dp[(i-1)%2][j-1], dp[(i-1)%2][j], dp[i%2][j-1]) + 1
                    else:
                        dp[i%2][j] = 0
                else:
                    dp[i%2][j] = matrix[i][j]
                max_space = min(dp[i%2][j], max_space)

        return max_space **2


matrix = [[1],[1],[1],[1],[1],[1],[1],[1],[1]]
solution = Solution()
res = solution.maxSquare_reduce_spcace(matrix)
print(res)