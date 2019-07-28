#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/27 11:36 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 488. Happy Number.py
# @Software: IntelliJ IDEA


class Solution:
    """
    @param n: An integer
    @return: true if this is a happy number or false
    """
    def isHappy(self, n):
        memo = set()
        while n != 1:
            memo.add(n)
            n = self.square_sum(n)
            if n in memo:
                return False

        return True


    def square_sum(self, num):
        sm = 0
        while num:
            sm += (num % 10) ** 2
            num = num // 10
        return sm
