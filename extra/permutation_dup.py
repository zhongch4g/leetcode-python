#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 10:05 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : permutation_dup.py
# @Software: IntelliJ IDEA

class Solution():
    def permutation_dup(self, nums):
        if nums is None or len(nums) == 0:
            return nums

        nums.sort()
        permutations = []
        visited = set()
        self.helper(nums, [], permutations, visited)
        print(permutations)

    def helper(self, nums, permutation, permutations, visited):
        if len(permutation) == len(nums):
            permutations.append(list(permutation))

        # divide problem
        for i in range(len(nums)):
            if i in visited:
                continue
            if i - 1 >= 0 and nums[i-1] == nums[i] and i - 1 not in visited:
                continue

            permutation.append(nums[i])
            visited.add(i)

            self.helper(nums, permutation, permutations, visited)

            permutation.pop()
            visited.remove(i)


solution = Solution()
solution.permutation_dup(["a", "a", "b"])

