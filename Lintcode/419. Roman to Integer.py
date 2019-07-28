#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/27 11:46 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 419. Roman to Integer.py
# @Software: IntelliJ IDEA


class Solution:
    """
    @param s: Roman representation
    @return: an integer
    """
    def romanToInt(self, s):
        romans = {'M': 1000, 'D': 500 , 'C': 100, 'L': 50, 'X': 10,'V': 5,'I': 1}

        prev = 0
        res = 0
        for i in range(len(s) - 1, -1, -1):
            cur = romans[s[i]]
            if cur < prev:
                res -= cur
            else:
                res += cur
            prev = cur
        return res
