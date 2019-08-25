#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/25 5:32 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 91. Decode Ways.py
# @Software: IntelliJ IDEA


class Solution:
    def numDecodings(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0
        dp = [0 for i in range(length + 1)]

        for i in range(length + 1):
            if i == 0:
                dp[i] = 1
                continue

            dp[i] = 0
            if i - 1 >= 0 and "1" <= s[i - 1] <= "9":
                dp[i] += dp[i - 1]

            if i - 2 >= 0 and "1" <= s[i - 2] + s[i - 1] <= "26":
                dp[i] += dp[i - 2]
        return dp[-1]


solution = Solution()
solution.numDecodings("226")