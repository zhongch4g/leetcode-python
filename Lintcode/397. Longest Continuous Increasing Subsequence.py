#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/24 9:32 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 397. Longest Continuous Increasing Subsequence.py
# @Software: IntelliJ IDEA


class Solution:
    """
    @param A: An array of Integer
    @return: an integer
    """
    def longestIncreasingContinuousSubsequence(self, A):
        length = len(A)
        if length == 0:
            return 0
        lr = self.LICS(A)
        A = A[::-1]
        rl = self.LICS(A)

        return max(lr, rl)


    def LICS(self, A):
        length = len(A)
        f = [0] * length
        res = 0
        for i in range(length):
            # case 1
            f[i] = 1

            # case 2
            if i > 0 and A[i] > A[i - 1]:
                f[i]  = f[i - 1] + 1

            res = max(res, f[i])
        return res
