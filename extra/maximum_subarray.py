#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/1 11:41 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : maximum_subarray.py
# @Software: IntelliJ IDEA

import sys
import heapq

class Solution:
    """
    @param nums: A list of integers
    @return: A integer indicate the sum of max subarray
    """
    def maxSubArray(self, nums):
        g, local = -sys.maxsize - 1, 0
        for i in range(len(nums)):
            local += nums[i]
            if local > g:
                g = local
            if local < 0:
                local = 0
        return  g

    # def max_subarray(self, nums):
    #     for i in range(1, len(nums)):
    #         nums[i] += nums[i-1]
    #     print(nums)
    #     heap = [0]
    #     maxinum = heap[0]
    #     for i in range(len(nums)):
    #         t = nums[i] - heap[0]
    #         if t > maxinum:
    #             maxinum = t
    #         heapq.heappush(heap, nums[i])
    #     return maxinum

    def max_subarray(self, nums):
        max_sum, min_sum = -sys.maxsize - 1, 0
        pre = 0
        for i in nums:
            pre += i
            max_sum = max(max_sum, pre - min_sum)
            min_sum = min(min_sum, pre)
        return max_sum


solution = Solution()
a = [-2, 2, -3, 4, -1, 2, 1, -5, 3]
b = [-2,2,-3,4,-1,2,1,-5,3]
c = [1, 2, 3, 4, 5, 100]
ans = solution.max_subarray(b)
print(ans)

