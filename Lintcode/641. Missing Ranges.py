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

        if not nums:
            results.append(self.rerange(lower, upper))
            return results

        # 切分第一段
        if lower + 1 != nums[0] or lower != nums[0]:
            string = self.rerange(lower, nums[0] - 1)
            if string:
                results.append(string)

        for i in range(1, len(nums)):
            string = self.rerange(nums[i-1] + 1, nums[i] - 1)
            if not string:
                continue
            results.append(string)

        if upper > nums[-1]:
            string = self.rerange(nums[-1] + 1, upper)
            if string:
                results.append(string)

        return results


    def rerange(self, left_point, right_point):
        if left_point > right_point:
            return None
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