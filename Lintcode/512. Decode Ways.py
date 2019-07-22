#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 9:40 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 512. Decode Ways.py
# @Software: IntelliJ IDEA


class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def numDecodings(self, s):
        if len(s) == 0:
            return 0

        dp = [0] * (len(s) + 1)
        dp[0] = 1

        for i in range(1, len(dp)):
            if s[i-1] != '0':
                dp[i] += dp[i-1]

            if i >= 2:
                curr = s[i-2] + s[i-1]
                # python chr ord
                if '1' <= curr <= '26':
                    dp[i] += dp[i-2]
        return dp[-1]


solution = Solution()
res = solution.numDecodings('10')
print(res)