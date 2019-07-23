#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/21 11:40 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 198. House Robber.py
# @Software: IntelliJ IDEA


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[1], nums[0])
        f = [0] * (len(nums) + 1)
        f[1] = nums[0]
        for i in range(1, len(nums) + 1):
            f[i] = max(f[i-2] + nums[i-1], f[i-1])
        return f[-1]