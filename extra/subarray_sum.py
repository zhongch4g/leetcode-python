#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/2 8:30 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : subarray_sum.py
# @Software: IntelliJ IDEA
import sys


class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        pre = 0
        prefix_hash = {0:-1}
        for i, num in enumerate(nums):
            pre += nums[i]
            if pre in prefix_hash.keys():
                return prefix_hash[pre] + 1, i
            prefix_hash[pre] = i


solution = Solution()
res = solution.subarraySum([-3, 1, 2, -3, 4])
print(res)