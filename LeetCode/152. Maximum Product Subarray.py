#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 5:55 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 152. Maximum Product Subarray.py
# @Software: IntelliJ IDEA



class Solution(object):

    def maxProduct(self, nums):
        if not nums:
            return None
        dp = [(nums[0], nums[0])]
        res = nums[0]
        for i in range(1, len(nums)):
            pre = dp[-1]
            imax = max(pre[0]*nums[i], pre[1]*nums[i], nums[i])
            imin = min(pre[0]*nums[i], pre[1]*nums[i], nums[i])
            dp.append((imax, imin))
            res = max(res, imax)
        print(dp)
        print(res)


solution = Solution()
solution.maxProduct([0, -1, -2, 0, 5, 3])
