#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/27 6:40 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 1075. Subarray Product Less Than K.py
# @Software: IntelliJ IDEA


class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: the number of subarrays where the product of all the elements in the subarray is less than k
    """
    def numSubarrayProductLessThanK(self, nums, k):
        product, i, result = 1, 0, 0

        for j, num in enumerate(nums):

            product *= num

            while i <= j and product >= k:
                product //= nums[i]
                i += 1

            result += j - i + 1

        return result
