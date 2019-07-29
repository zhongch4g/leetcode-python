#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/28 1:48 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 641. Missing Ranges.py
# @Software: IntelliJ IDEA


class Solution:
    """
    @param: nums: a sorted integer array
    @param: lower: An integer
    @param: upper: An integer
    @return: a list of its missing ranges
    """
    def findMissingRanges(self, nums, lower, upper):
        results = []
        if not nums or lower > nums[-1] or upper < nums[0]:
            results.append(self.rerange(lower, upper))
            return results


    def rerange(self, left_point, right_point):
        if left_point == right_point:
            return str(left_point)
        else:
            return str(left_point) + "->" + str(right_point)




nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
solution = Solution()
# solution.findMissingRanges(nums, lower, upper)
solution.rerange(0, 10)