#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/8 8:33 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 377. Combination Sum IV.py
# @Software: IntelliJ IDEA


import sys
class Solution:
    def combinationSum4(self, nums, target: int) -> int:
        nums.sort()
        return self.search(nums, target, {})

    def search(self, nums, target, memo):
        if target in memo:
            return memo[target]

        if target == 0:
            return 1

        if target < 0:
            return 0

        count = 0
        for num in nums:
            count += self.search(nums, target - num, memo)

        memo[target] = count
        return count
