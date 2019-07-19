#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/19 11:44 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 560. Subarray Sum Equals K.py
# @Software: IntelliJ IDEA


class Solution:
    def subarraySum(self, nums, k):
        nsum = 0
        # 保存值和索引
        d = {0:1}
        count = 0
        for i, num in enumerate(nums):
            nsum += num
            if nsum - k in d:
                count += d[nsum - k]
            d[nsum] = d.get(nsum, 0) + 1
        return count


nums = [1,1,1]
k = 2
solution = Solution()
res = solution.subarraySum(nums, k)
print(res)

