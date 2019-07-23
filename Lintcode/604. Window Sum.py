#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/23 5:40 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 604. Window Sum.py
# @Software: IntelliJ IDEA


class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        index = 0
        curr_sum = 0
        result = []
        for num in nums:
            curr_sum += num
            if index + 1 >= k:
                result.append(curr_sum)
                curr_sum -= nums[index-k+1]

            index += 1

        print(result)


array = [0,0,10,2,-7,8,5]
k = 10
solution = Solution()
solution.winSum(array, k)