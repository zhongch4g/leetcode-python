#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/26 2:32 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : merge_two_sorted_interval_lists.py
# @Software: IntelliJ IDEA


"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# Lintcode 839
class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """
    def mergeTwoInterval(self, list1, list2):
        index1, index2 = 0, 0
        intervals = []
        while index1 < len(list1) and index2 < len(list2):
            if list1[index1].start <= list2[index2].start:
                self.merge(list1[index1], intervals)
                index1 += 1
            else:
                self.merge(list2[index2], intervals)
                index2 += 1

        while index1 < len(list1):
            self.merge(list1[index1], intervals)
            index1 += 1

        while index2 < len(list2):
            self.merge(list2[index2], intervals)
            index2 += 1

        return intervals

    def merge(self, node, intervals):
        if not intervals:
            intervals.append(node)
            return

        end_node = intervals[-1]

        if end_node.end < node.start:
            intervals.append(node)

        intervals[-1].end = max(node.end, end_node.end)






