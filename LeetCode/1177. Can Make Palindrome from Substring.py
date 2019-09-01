#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/1 12:20 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 1177. Can Make Palindrome from Substring.py
# @Software: IntelliJ IDEA


class Solution:
    def canMakePaliQueries(self, s: str, queries):

        prefix = [[0] * 26 for i in range(len(s) + 1)]

        for i in range(len(s)):
            prefix[i + 1] = list(prefix[i])
            prefix[i + 1][ord(s[i]) - ord('a')] += 1

        res = []
        for left, right, k in queries:
            s = 0
            for j in range(26):
                s += (prefix[right + 1][j] - prefix[left][j]) % 2
            res.append(s // 2 <= k)
        return res

