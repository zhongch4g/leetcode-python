#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 10:45 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 30. Insert Interval.py
# @Software: IntelliJ IDEA


"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: Sorted interval list.
    @param newInterval: new interval.
    @return: A new interval list.
    """
    def insert(self, intervals, newInterval):
        if not intervals:
            return intervals.append(newInterval)
        if not newInterval:
            return intervals
        intervals.append(newInterval)
        intervals.sort(key=lambda x:x.start)

        res = []
        for interval in intervals:
            if not res:
                res.append(interval)
            else:
                last = res[-1]
                if last.end < interval.start:
                    res.append(interval)
                else:
                    last.end = max(last.end, interval.end)
        return res

