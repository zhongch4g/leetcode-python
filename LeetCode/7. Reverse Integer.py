#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 1:59 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 7. Reverse Integer.py
# @Software: IntelliJ IDEA


class Solution:
    def reverse(self, x):
        print([1,-1][x < 0])
        sign = [1,-1][x < 0]
        rst = sign * int(str(abs(x))[::-1])
        return rst if -(2**31)-1 < rst < 2**31 else 0


solution = Solution()
res = solution.reverse(123)
print(res)