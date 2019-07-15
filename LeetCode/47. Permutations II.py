#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/14 5:22 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 47. Permutations II.py
# @Software: IntelliJ IDEA


class Solution:
    def permuteUnique(self, nums):

        permutations = []
        memo = set()
        nums.sort()
        self.search(nums, [], permutations, memo)
        print(permutations)

    def search(self, nums, permutation, permutations, memo):

        if len(nums) == len(permutation):
            permutations.append(list(permutation))
            return

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1] and i - 1 not in memo:
                continue
            if i in memo:
                continue

            memo.add(i)
            permutation.append(nums[i])
            self.search(nums, permutation, permutations, memo)
            memo.remove(i)
            permutation.pop()



array = [3,3,0,3]
solution = Solution()
solution.permuteUnique(array)