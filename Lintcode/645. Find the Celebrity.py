#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/27 10:47 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 645. Find the Celebrity.py
# @Software: IntelliJ IDEA


"""
The knows API is already defined for you.
@param a, person a
@param b, person b
@return a boolean, whether a knows b
you can call Celebrity.knows(a, b)
"""

class Celebrity:
    def knows(self, candidate, i):
        return -1

class Solution:
    # @param {int} n a party with n people
    # @return {int} the celebrity's label or -1
    def findCelebrity(self, n):
        if n <= 0:
            return -1
        if n == 1:
            return 0

        candidate = 0
        for i in range(n):
            if Celebrity.knows(candidate, i):
                candidate = i

        for i in range(n):
            if i != candidate and Celebrity.knows(candidate, i):
                return -1

            if i != candidate and not Celebrity.knows(i, candidate):
                return -1

        return candidate

