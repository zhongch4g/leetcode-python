#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/18 8:07 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : longest_one_greater_zero.py
# @Software: IntelliJ IDEA

import sys
class Solution:
    def longest_one_greater_zero(self, nums):


        nsum = 0
        d = {0:-1}
        length = 0
        for i, num in enumerate(nums):
            nsum += 1 if num == 1 else -1
            if nsum not in d:
                d[nsum] = i

            if nsum - 1 in d and i - d[nsum - 1] > length:
                length = i - d[nsum - 1]

        return len(nums) if nsum > 0 else length



nums = [1, 0, 0, 0, 1, 0, 1, 0, 1]
nums2 = [0,0,1,0,0,1,1,1]
solution = Solution()
res = solution.longest_one_greater_zero(nums2)
print(res)