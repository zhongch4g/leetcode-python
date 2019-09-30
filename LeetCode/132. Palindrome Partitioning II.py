#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/30 4:49 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 132. Palindrome Partitioning II.py
# @Software: IntelliJ IDEA


import sys
class Solution:
    def minCut(self, s: str) -> int:
        length = len(s)
        if length == 0:
            return 0
        is_palin = [[False] * length for i in range(length)]

        for c in range(length - 1):
            # even
            i, j = c, c + 1
            while i >= 0 and j < length and s[i] == s[j]:
                is_palin[i][j] = True
                i -= 1
                j += 1

        for o in range(length):
            # odd
            i, j = o, o
            while i >= 0 and j < length and s[i] == s[j]:
                is_palin[i][j] = True
                i -= 1
                j += 1

        mincut = [0 for i in range(length + 1)]
        for i in range(1, length + 1):
            mincut[i] = sys.maxsize
            for j in range(i):
                if is_palin[j][i - 1]:
                    mincut[i] = min(mincut[i], mincut[j] + 1)
        # Attention: Cut how many times, not how many palindrome
        return mincut[length] - 1
