#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/29 12:46 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 209. Minimum Size Subarray Sum.py
# @Software: IntelliJ IDEA


import sys
class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        length = len(nums)
        if length == 0:
            return 0

        area_sum = 0
        i = 0
        minisize = sys.maxsize
        for j in range(length):
            area_sum += nums[j]

            while area_sum >= s:
                minisize = min(minisize, j - i + 1)
                area_sum -= nums[i]
                i += 1

        return minisize if minisize != sys.maxsize else 0
