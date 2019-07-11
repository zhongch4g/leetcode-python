#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/10 8:37 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 15. 3Sum.py
# @Software: IntelliJ IDEA


class Solution:
    def threeSum(self, nums):
        """
        suppose a < b < c
        :param nums:
        :return:
        """
        nums.sort()
        results = []
        print(nums)
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    results.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] > target:
                    r -= 1
                else:
                    l += 1
        return results




nums = [1,-1,-1,0]
solution = Solution()
res = solution.threeSum(nums)
print(res)