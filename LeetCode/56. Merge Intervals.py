#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 3:04 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 56. Merge Intervals.py
# @Software: IntelliJ IDEA


class Solution:
    def merge(self, intervals):
        if not intervals:
            return intervals
        intervals.sort(key = lambda x: x[0])
        result = []
        for interval in intervals:
            if not result:
                result.append(interval)
            if result[-1][1] < interval[0]:
                result.append(interval)
            result[-1][1] = max(result[-1][1], interval[1])
        return result


intervals = [[1,4],[2,3]]
solution = Solution()
res = solution.merge(intervals)
print(res)
