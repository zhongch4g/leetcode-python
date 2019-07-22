#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/27 9:49 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : k_sum.py
# @Software: IntelliJ IDEA

class Solution:
    def combination_sum(self, nums, target):
        nums = list(set(nums))
        nums.sort()
        result = []
        self.search(nums, target, 0, [], result)
        return result

    def search(self, nums, target, index, combination, result):
        if target == 0:
            result.append(list(combination))
            return
        for i in range(index, len(nums)):
            if target < nums[i]:
                return
            combination.append(nums[i])
            self.search(nums, target - nums[i], i, combination, result)
            combination.pop()

    def k_sum(self, nums, k, target):
        result = [0]
        self.search1(nums, k, target, [], result)
        return result[0]


    def search1(self, nums, k, target, l, result):
        if sum(l) == target and len(l) == k:
            result[0] += 1
            return

        if sum(l) > target or len(nums) <= 0 or len(l) >= k:
            return
        else:
            l.append(nums[0])
            self.search1(nums[1:], k, target, l, result)
            l.remove(nums[0])
            self.search1(nums[1:], k, target, l, result)


solution = Solution()
res = solution.combination_sum([7,1,2,5,1,6,10], 8)
print("res: ", res)
# k_sum = solution.k_sum([1, 2, 3, 4], 2, 5)
# print("k_sum: ", k_sum)