#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/11 3:38 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : permutationII.py
# @Software: IntelliJ IDEA


class Solution:
    """
    @param: :  A list of integers
    @return: A list of unique permutations
    """

    def permuteUnique(self, nums):
        permutations = []
        visited = set()
        nums.sort()
        self.helper(nums, [], permutations, visited)
        print(permutations)

    def helper(self, nums, permutation, permutations, visited):

        if len(permutation) == len(nums):
            permutations.append(list(permutation))
            return

        for i in range(len(nums)):
            if i - 1 >= 0 and nums[i] == nums[i-1] and i - 1 not in visited:
                continue

            if i in visited:
                continue

            permutation.append(nums[i])
            visited.add(i)

            self.helper(nums, permutation, permutations, visited)

            permutation.pop()
            visited.remove(i)

solution = Solution()
solution.permuteUnique([3, 3, 0, 3])