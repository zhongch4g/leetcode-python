#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/19 12:39 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 1124. Longest Well-Performing Interval.py
# @Software: IntelliJ IDEA


class Solution:
    def longestWPI(self, hours):

        nsum = 0
        d = {0:-1}
        length = 0
        for i, hour in enumerate(hours):
            nsum += 1 if hour > 8 else -1
            if nsum not in d:
                d[nsum] = i

            if nsum - 1 in d and i - d[nsum - 1] > length:
                length = i - d[nsum - 1]

        return len(hours) if nsum > 0 else length


solution = Solution()
res = solution.longestWPI([9,9,9])
print(res)