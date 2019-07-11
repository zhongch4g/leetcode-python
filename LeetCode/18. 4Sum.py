#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/11 11:27 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 18. 4Sum.py
# @Software: IntelliJ IDEA


class Solution:
    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []
        nums.sort()
        res = []
        max_num = nums[-1]
        for i in range(len(nums)-3):
            a = nums[i]
            ### Attention
            if a > 0 and a >= target:
                break
            if 4 * a > target:
                break
            if a + 3 * max_num < target:
                continue
            ### End Attention...
            if i > 0 and nums[i] == nums[i-1]:
                continue

            for j in range(i + 1, len(nums)-2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                b = nums[j]

                l, r = j + 1, len(nums) - 1
                while l < r:
                    cur = a + b + nums[l] + nums[r]
                    if cur == target:
                        res.append([a, b, nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    elif cur > target:
                        r -= 1
                    else:
                        l += 1
        print(res)


solution = Solution()
solution.fourSum([0,0,0,0], 0)