#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/1 6:21 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 287. Find the Duplicate Number.py
# @Software: IntelliJ IDEA


import sys
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) > 1:
            slow = nums[0]
            fast = nums[nums[0]]
            while slow != fast:
                slow = nums[slow]
                fast = nums[nums[fast]]

            slow = 0
            while slow != fast:
                slow = nums[slow]
                fast = nums[fast]
            return slow
        return -1