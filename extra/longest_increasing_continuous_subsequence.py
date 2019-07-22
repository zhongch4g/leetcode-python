#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/14 8:52 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : longest_increasing_continuous_subsequence.py
# @Software: IntelliJ IDEA


step_x = [-1, 1, 0, 0]
step_y = [0, 0, 1, -1]

class Solution:
    def longest_increasing_continuous_subsequence(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        n = len(matrix)
        m = len(matrix[0])
        dp = [[1] * m for i in range(n)]
        flag = [[0] * m for i in range(n)]
        res = 0
        for i in range(n):
            for j in range(m):
                dp[i][j] = self.search(matrix, i, j, flag, dp)
                res = max(res, dp[i][j])
        return res

    def search(self, matrix, i, j, flag, dp):
        if flag[i][j] == 1:
            return dp[i][j]

        ans = 1
        for delta in range(4):
            _x = i + step_x[delta]
            _y = j + step_y[delta]

            if self.is_valid(matrix, _x, _y) and matrix[_x][_y] < matrix[i][j]:
                ans = max(ans, self.search(matrix, _x, _y, flag, dp) + 1)
                # dp[i][j] = max(dp[i][j], self.search(matrix, _x, _y, flag, dp) + 1)
        flag[i][j] = 1
        dp[i][j] = ans
        return ans



    def is_valid(self, matrix, x, y):
        return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])



matrix = [[1, 2, 3, 4, 5],
          [16, 17, 24, 23, 6],
          [15, 18, 25, 22, 7],
          [14, 19, 20, 21, 8],
          [13, 12, 11, 10, 9]]
solution = Solution()
res = solution.longest_increasing_continuous_subsequence(matrix)
print(res)