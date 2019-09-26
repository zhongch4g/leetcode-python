#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/25 8:54 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 354. Russian Doll Envelopes.py
# @Software: IntelliJ IDEA

# TLE O(n^2) 最优是O(nlogn)
import functools
class Solution:
    def maxEnvelopes(self, envelopes) -> int:
        if not envelopes:
            return 0
        m = len(envelopes)

        envelopes.sort(key=functools.cmp_to_key(self.cmp))
        # envelopes.sort(key=lambda e: (e[0], e[1]))

        f = [0 for i in range(m)]
        res = 0
        for i in range(m):
            f[i] = 1
            for j in range(i + 1):
                if envelopes[i][0] > envelopes[j][0] and envelopes[i][1] > envelopes[j][1]:
                    f[i] = max(f[i], f[j] + 1)
            res = max(res, f[i])
        return res


    def cmp(self, e1, e2):
        if e1[0] == e2[0]:
            return e1[1] - e2[1]
        else:
            return e1[0] - e2[0]


