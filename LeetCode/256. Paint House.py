#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/22 10:21 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 256. Paint House.py
# @Software: IntelliJ IDEA


import sys
class Solution:
    def minCost(self, costs) -> int:
        if not costs:
            return 0

        paint = [3 * [0] for i in range(len(costs) + 1)]
        for i in range(1, len(costs) + 1):
            for j in range(3):
                paint[i][j] = sys.maxsize
                for k in range(3):
                    if j == k:
                        continue
                    paint[i][j] = min(paint[i - 1][k] + costs[i - 1][j], paint[i][j])
        return min(paint[-1][0], paint[-1][1], paint[-1][2])