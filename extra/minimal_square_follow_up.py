#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/14 7:42 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : minimal_square_follow_up.py
# @Software: IntelliJ IDEA


class Solution:
    """
    @param matrix: a matrix of 0 and 1
    @return: an integer
    """
    def max_square_follow_up(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        if n <= 0 or m <= 0:
            return 0


        max_len = -1
        dp = [[-1] * m for i in range(n)]
        for i in range(n):
            dp[i][0] = matrix[i][0]
            max_len = max(max_len, dp[i][0])
            for j in range(1, m):
                if i > 0:
                    if matrix[i][j] == 1:
                        dp[i][j] = min(dp[i-1][j-1], self.up_zero(matrix, i-1, j), self.left_zero(matrix, i, j-1)) + 1
                    else:
                        dp[i][j] = 0
                else:
                    dp[i][j] = matrix[i][j]
                max_len = max(max_len, dp[i][j])
        print(dp)
        return max_len ** 2


    def up_zero(self, matrix, i, j):
        cnt = 0
        for it in range(i+1):
            if matrix[i-it][j] != 0:
                return cnt
            cnt += 1
        return cnt

    def left_zero(self, matrix, i, j):
        cnt = 0
        for it in range(j+1):
            if matrix[i][j-it] != 0:
                return cnt
            cnt += 1
        return cnt

matrix = [[1, 0, 1, 1, 0],
          [1, 0, 0, 1, 0],
          [1, 1, 0, 0, 0],
          [1, 0, 1, 1, 0]]
solution = Solution()
res = solution.max_square_follow_up(matrix)
print(res)