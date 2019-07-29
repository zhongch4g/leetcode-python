#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/27 7:13 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 417. Valid Number.py
# @Software: IntelliJ IDEA


class Solution:
    """
    @param s: the string that represents a number
    @return: whether the string is a valid number
    """
    def isNumber(self, s):

        s = s.strip()
        length = len(s)
        # add dummy
        s = s + ' '

        idx = 0
        if s[idx] == '+' or s[idx] == '-':
            idx += 1

        # check point
        ndigit, ndot = 0, 0
        while '0' <= s[idx] <= '9' or s[idx] == '.':
            if '0' <= s[idx] <= '9':
                ndigit += 1
            if s[idx] == '.':
                ndot += 1
            idx += 1
        if ndigit <= 0 or ndot > 1:
            return False

        if s[idx] == 'e':
            idx += 1
            if s[idx] == '+' or s[idx] == '-':
                idx += 1

            if idx == length:
                return False

            while '0' <= s[idx] <= '9':
                idx += 1

        return idx == length