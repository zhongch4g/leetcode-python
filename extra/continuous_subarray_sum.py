#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/2 8:42 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : continuous_subarray_sum.py
# @Software: IntelliJ IDEA
import sys


class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySum(self, A):
        max_sum, pre = -sys.maxsize - 1, 0
        ti = 0
        mi, mj = 0, 0
        for i in range(len(A)):
            pre += A[i]
            if pre > max_sum:
                max_sum = pre
                mi = ti
                mj = i
            if pre < 0:
                pre = 0
                ti = i + 1
        return [mi, mj]