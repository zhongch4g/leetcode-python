#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/17 3:14 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : house_robber.py
# @Software: IntelliJ IDEA

class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber(self, A):
        if not A:
            return 0
        if len(A) <= 2:
            return max(A)

        # f = [0] * len(A)
        f = [0] * 3
        f[0], f[1] = A[0], max(A[0], A[1])
        for i in range(2, len(A)):
            f[i%3] = max(f[(i-1)%3], f[(i-2)%3]+A[i])
        print(f)
        return f[(len(A)-1)%3]


solution = Solution()
res = solution.houseRobber([5, 2, 1, 3])
print(res)