#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 6:00 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 62. Unique Paths.py
# @Software: IntelliJ IDEA


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[1] * n for i in range(2)]

        for i in range(1, m):
            for j in range(1, n):
                dp[i%2][j] = dp[(i-1)%2][j] + dp[i%2][j-1]
        return dp[(m-1)%2][n-1]

