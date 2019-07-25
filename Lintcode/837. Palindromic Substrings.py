#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/24 2:05 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 837. Palindromic Substrings.py
# @Software: IntelliJ IDEA


class Solution:
    """
    @param str: s string
    @return: return an integer, denote the number of the palindromic substrings
    """
    # Time Limit Exceeded
    def countPalindromicSubstrings(self, str):
        count = 0
        for i in range(1, len(str) + 1):
            idx1, idx2 = 0, i
            while idx2 <= len(str):

                if str[idx1:idx2] == str[idx1:idx2][::-1]:
                    count += 1
                idx1 += 1
                idx2 += 1
        return count

    def countPalindromicSubstrings2(self, str):
        n = len(str)
        dp = [[0] * n for i in range(n)]
        count = 0
        for i in range(n):
            for j in range(i + 1):
                if str[i] == str[j] and (i - j <= 2 or dp[j+1][i-1] == 1):
                    dp[j][i] = 1

                if dp[j][i]:
                    count += 1
        return count



solution = Solution()
