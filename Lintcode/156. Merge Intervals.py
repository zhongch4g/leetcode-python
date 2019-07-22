#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 10:35 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 156. Merge Intervals.py
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
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # write your code here
        if len(intervals) == 0:
            return []

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