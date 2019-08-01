#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/1 5:33 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 238. Product of Array Except Self.py
# @Software: IntelliJ IDEA


class Solution(object):
    # func one
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1] * len(nums)
        right = [1] * len(nums)

        # calc i-th left product
        for i in range(1, len(nums)):
            left[i] = nums[i - 1] * left[i - 1]

        for j in range(len(nums) - 2, -1, -1):
            right[j] = right[j + 1] * nums[j + 1]

        result = []
        for i in range(len(nums)):
            result.append(left[i] * right[i])
        return result


    # func one
    def productExceptSelf1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1] * len(nums)

        # calc i-th left product
        for i in range(1, len(nums)):
            result[i] = nums[i - 1] * result[i - 1]

        R = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] = R * result[i]
            R = R * nums[i]

        return result


