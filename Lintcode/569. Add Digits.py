#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/27 11:28 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 569. Add Digits.py
# @Software: IntelliJ IDEA

import sys
class Solution:
    """
    @param num: a non-negative integer
    @return: one digit
    """
    def addDigits(self, num):

        while num >= 10:
            cur = 0
            while num:
                cur += num % 10
                num = num // 10
            num = cur
        return num



