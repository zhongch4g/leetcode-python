#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/28 10:45 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 428. Pow(x, n).py
# @Software: IntelliJ IDEA


class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x, n):
        # if n < 0:
        if n < 0:
            x = 1 / x
            n = -n
        temp = x
        res = 1
        while n != 0:
            if n & 1 == 1:
                res *= temp
            n = n >> 1
            temp *= temp
        return res