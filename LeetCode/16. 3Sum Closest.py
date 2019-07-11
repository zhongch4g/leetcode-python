#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/11 10:27 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 16. 3Sum Closest.py
# @Software: IntelliJ IDEA

import sys


class Solution:
    def threeSumClosest(self, nums, target):
        res = None
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if res is None or abs(s - target) < abs(res - target):
                    res = s
                if s <= target:
                    l += 1
                else:
                    r -= 1
        return res


solution = Solution()
res = solution.threeSumClosest([-1, 2, 1, -4], 1)
print(res)