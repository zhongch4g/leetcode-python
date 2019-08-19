#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 1:39 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 254. Factor Combinations.py
# @Software: IntelliJ IDEA


class Solution:
    def getFactors(self, n: int):
        combinations = []

        self.search(combinations, [], n, 2)
        return combinations

    def search(self, combinations, combination, remain, fac):

        if remain == 1:
            if len(combination) > 1:
                combinations.append(list(combination))

        for i in range(fac, remain + 1):

            if remain % i == 0:

                combination.append(i)
                self.search(combinations, combination, remain // i, i)
                combination.pop()
import math
class Solution2:
    def getFactors(self, n: int):
        combinations = []

        self.search(combinations, [], n, 2)
        return combinations

    def search(self, combinations, combination, remain, fac):

        # if remain == 1:
        #     if len(combination) > 1:
        #         combinations.append(list(combination))

        for i in range(fac, int(math.sqrt(remain)) + 1):

            if remain % i == 0:

                combination.append(i)
                combinations.append(combination + [int(remain // i)])
                self.search(combinations, combination, remain // i, i)
                combination.pop()

solution = Solution2()
res = solution.getFactors(12)
print(res)