#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/27 11:50 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 586. Sqrt(x) II.py
# @Software: IntelliJ IDEA


class Solution:
    """
    @param x: a double
    @return: the square root of x
    """
    def sqrt(self, x):
        if x < 0:
            return -1

        if x >= 1:
            start, end = 1, x
        else:
            start, end = x, 1

        while end - start > 1e-10:
            mid = (start + end) / 2
            if mid * mid < x:
                start = mid
            else:
                end = mid

        return start


    def sqrt1(self, x):
        # newton

        n0 = 1.0
        e = 1e-10
        while abs(n0 * n0 - x) > e:
            n0 = 1/2.0 * (n0 + x / n0)
        return n0



solution = Solution()
solution.sqrt(2)