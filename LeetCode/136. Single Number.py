#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/19 6:29 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 136. Single Number.py
# @Software: IntelliJ IDEA


class Solution:
    def singleNumber(self, nums):
        if not nums:
            return 0
        result = 0
        for i in range(len(nums)):
            result ^= nums[i]
        return result
