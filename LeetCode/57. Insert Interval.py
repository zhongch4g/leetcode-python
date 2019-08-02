#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/1 9:32 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 57. Insert Interval.py
# @Software: IntelliJ IDEA


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if not intervals:
            result.append(newInterval)
            return result
        intervals.append(newInterval)
        intervals.sort(key=lambda x: (x[0], x[1]))

        for interval in intervals:
            if not result:
                result.append(interval)
                continue
            last = result[-1]
            if interval[0] > last[1]:
                result.append(interval)
            else:
                last[1] = max(interval[1], last[1])
        return result