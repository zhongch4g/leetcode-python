#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/13 10:48 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 32. Longest Valid Parentheses.py
# @Software: IntelliJ IDEA


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) <= 1:
            return 0

        dp = [0] * len(s)

        max_len = 0
        minus = 0
        for i in range(1, len(s)):
            if s[i] == ')':

                if s[i-1] == '(':
                    dp[i] = dp[i - 2] + 2 if i >= 2 else 2
                elif i - dp[i - 1] > 0 and s[i - dp[i - 1] - 1] == '(':
                    dp[i] = dp[i - 1] + (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0) + 2

            max_len = max(max_len, dp[i])
        print(dp)
        print(max_len)


solution = Solution()
s1 = "()(()"
s2 = "()()()()()"
solution.longestValidParentheses(s2)
