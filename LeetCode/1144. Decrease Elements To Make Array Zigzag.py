#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/3 10:06 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 1144. Decrease Elements To Make Array Zigzag.py
# @Software: IntelliJ IDEA


import sys
class Solution:
    def movesToMakeZigzag(self, nums):

        length = len(nums)

        if length == 1:
            return 0

        zigzag_even = 0
        zigzag_odd = 0

        for i in range(length):
            if i % 2 == 0:
                if i == 0 and nums[i + 1] <= nums[i]:
                    zigzag_even += nums[i] - nums[i + 1] + 1
                elif i == length - 1 and nums[i - 1] <= nums[i]:
                    zigzag_even += nums[i] - nums[i - 1] + 1
                elif 0 < i < length - 1 and (nums[i] >= nums[i - 1] or nums[i] >= nums[i + 1]):
                    zigzag_even += nums[i] - min(nums[i + 1], nums[i - 1]) + 1
            else:
                if i == 0 and nums[i + 1] <= nums[i]:
                    zigzag_odd += nums[i] - nums[i + 1] + 1
                elif i == length - 1 and nums[i - 1] <= nums[i]:
                    zigzag_odd += nums[i] - nums[i - 1] + 1
                elif 0 < i < length - 1 and (nums[i] >= nums[i - 1] or nums[i] >= nums[i + 1]):
                    zigzag_odd += nums[i] - min(nums[i + 1], nums[i - 1]) + 1
        return min(zigzag_even, zigzag_odd)