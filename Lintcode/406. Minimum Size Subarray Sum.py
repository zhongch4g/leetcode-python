#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/25 7:15 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 406. Minimum Size Subarray Sum.py
# @Software: IntelliJ IDEA


import sys
class Solution:
    """
    @param nums: an array of integers
    @param s: An integer
    @return: an integer representing the minimum size of subarray
    """
    def minimumSize(self, nums, s):

        if not nums:
            return -1

        cur_sum = 0
        j = 0
        length = sys.maxsize
        for i in range(len(nums)):
            while j < len(nums) and cur_sum < s:
                cur_sum += nums[j]
                j += 1
            if cur_sum >= s:
                length = min(length, j - i)
            cur_sum -= nums[i]
        if length == sys.maxsize:
            return -1
        return length


nums = [2,3,1,2,4,3]
s = 7
solution = Solution()
solution.minimumSize(nums, s)
