#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 11:12 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : merge_k_sorted_interval_lists.py
# @Software: IntelliJ IDEA

import heapq

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Pair:
    def __init__(self, row, col, interval):
        self.row = row
        self.col = col
        self.interval = interval

    def __lt__(self, other):
        return self.interval.start < other.interval.start

class Solution:
    """
    @param intervals: the given k sorted interval lists
    @return:  the new sorted interval list
    """
    def mergeKSortedIntervalLists(self, intervals):
        heap = []
        # init heap
        for i in range(len(intervals)):
            if intervals[i]:
                heap.append(Pair(i, 0, intervals[i][0]))

        heapq.heapify(heap)

        result = []
        while heap:
            pair = heapq.heappop(heap)
            result.append(pair.interval)

            if pair.col + 1 < len(intervals[pair.row]):
                heapq.heappush(heap, Pair(pair.row, pair.col + 1, intervals[pair.row][pair.col + 1]))

        return self.merge(result)

    def merge(self, intervals):
        if not intervals:
            return intervals

        result = [intervals[0]]
        start = 1
        while start < len(intervals):
            last_interval = result[-1]
            if last_interval.end < intervals[start].start:
                result.append(intervals[start])
            result[-1].end = max(result[-1].end, intervals[start].end)
            start += 1
        return result

solution = Solution()
result = solution.mergeKSortedIntervalLists(
                                    [[Interval(1,3),Interval(4,7),Interval(6,8)],
                                    [Interval(1,2),Interval(9,10)]]
                                   )
for interval in result:
    print(interval.start, interval.end)
