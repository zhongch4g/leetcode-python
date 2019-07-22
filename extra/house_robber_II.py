#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/17 3:38 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : house_robber_II.py
# @Software: IntelliJ IDEA


class Solution:
    """
    @param nums: An array of non-negative integers.
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber2(self, nums):
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        # cicle, there are two situation, so that we can divide it into two parts
        nums1 = nums[1:]
        nums2 = nums[:-1]
        return max(self.houseRobber(nums1), self.houseRobber(nums2))

    def houseRobber(self, nums):
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        # Initialization
        f = [0]*3
        f[0], f[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            f[i%3] = max(f[(i-1)%3], f[(i-2)%3]+nums[i])
        return f[(len(nums)-1)%3]


solution = Solution()
res = solution.houseRobber2([1,3,2,1,5])
print(res)