#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/2 10:48 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : subsets_with_dup.py
# @Software: IntelliJ IDEA
class Solution:

    def subsetsWithDup(self, nums: 'List[int]') -> 'List[List[int]]':
        if nums is None:
            return nums
        if len(nums) == 0:
            return nums
        # In order to duplicate number in nums
        nums.sort()
        combinations = []
        self.dfs(nums, 0, [], combinations)
        return combinations

    def dfs(self, nums, index, combination, combinations):
        combinations.append(list(combination))

        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            combination.append(nums[i])
            self.dfs(nums, i + 1, combination, combinations)
            combination.pop()


solution = Solution()
combinations = solution.subsetsWithDup([4,4,4,1,4])
print(combinations)
