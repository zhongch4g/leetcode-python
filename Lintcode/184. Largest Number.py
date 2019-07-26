#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/25 7:34 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 184. Largest Number.py
# @Software: IntelliJ IDEA
from functools import cmp_to_key


class Solution:
    """
    @param nums: A list of non negative integers
    @return: A string
    """
    def largestNumber(self, nums):
        # write your code here
        nums.sort(key=cmp_to_key(lambda x, y: 1 if str(x)+str(y) < str(y)+str(x) else -1))
        print(nums)
        if nums[0] == 0:
            return '0'
        return "".join([str(x) for x in nums])



solution = Solution()
solution.largestNumber([1,20,23,4,8])