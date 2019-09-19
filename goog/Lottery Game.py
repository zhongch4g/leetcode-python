#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/18 7:46 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : Lottery Game.py
# @Software: IntelliJ IDEA

import sys
class Solution:
    def lottery_game(self, coupons):
        h = {}
        minimum = sys.maxsize
        for i in range(len(coupons)):
            if coupons[i] in h:
                minimum = min(minimum, i - h[coupons[i]] + 1)
            h[coupons[i]] = i
        return minimum if minimum != sys.maxsize else -1

solution = Solution()
res = solution.lottery_game([5, 3, 4, 2, 3, 4, 5, 7])
print(res)