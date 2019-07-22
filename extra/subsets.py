#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/1 3:25 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : subsets.py
# @Software: IntelliJ IDEA

class Solution:
    """
    @param nums: A set of numbers
    @return: A list of lists
    """
    def subsets(self, nums):
        nums = sorted(nums)
        combinations = []
        nums.sort()
        self.dfs(nums, 0, [], combinations)
        return combinations

    def dfs(self, nums, index, combination, combinations):
        combinations.append(list(combination))

        for i in range(index, len(nums)):
            combination.append(nums[i])
            self.dfs(nums, i + 1, combination, combinations)
            combination.pop()

    def subsets1(self, nums: 'List[int]') -> 'List[List[int]]':
        res = [[]]
        for n in nums:
            res += [[n] + r for r in res]
        return res


solution = Solution()
combination = solution.subsets1([1, 2, 3])
print(combination)