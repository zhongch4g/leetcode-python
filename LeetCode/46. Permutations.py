#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/14 5:03 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 46. Permutations.py
# @Software: IntelliJ IDEA


class Solution:
    def permute(self, nums):
        if not nums:
            return []
        nums.sort()
        combinations = []
        self.search(nums, [], combinations)
        print(combinations)


    def search(self, nums, combination, combinations):
        if len(combination) == len(nums):
            combinations.append(list(combination))
            return

        for i in range(len(nums)):
            if nums[i] in combination:
                continue
            combination.append(nums[i])
            self.search(nums, combination, combinations)
            combination.pop()


solution = Solution()
solution.permute([1, 2, 3])



