#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 3:15 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 640. One Edit Distance.py
# @Software: IntelliJ IDEA


class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    """
    def isOneEditDistance1(self, s, t):
        m = len(s)
        n = len(t)
        if abs(m - n) > 1:
            return False

        if m > n:
            return self.isOneEditDistance1(t, s)
        for i in range(m):
            if s[i] != t[i]:
                if m == n:
                    return s[i + 1:] == t[i + 1:]
                return s[i:] == t[i + 1:]
        # 去掉了长度相等的情况
        return m != n



    def isOneEditDistance(self, s, t):

        if not s and not t:
            return False
        # write your code here
        m = len(s) + 1
        n = len(t) + 1

        dp = [[0] * m for i in range(n)]

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                if j > 0 and i == 0:
                    dp[i][j] = dp[i][j - 1] + 1
                    continue

                if i > 0 and j == 0:
                    dp[i][j] = dp[i - 1][j] + 1
                    continue

                if s[j - 1] == t[i - 1]:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[n - 1][m - 1] == 1


solution = Solution()
res = solution.isOneEditDistance1('ab', 'a')
print(res)