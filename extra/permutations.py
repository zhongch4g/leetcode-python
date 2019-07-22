#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/8 9:35 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : permutations.py
# @Software: IntelliJ IDEA

class Solution():
    """
    和subsets的关系是:
    permutation是凑齐再加到答案上; 而subsets是中间结果也存.
    permutation是可以回头取的, 但是不能重复取, 所以没有startIndex.
    """
    def permutations(self, nums):
        if nums is None or len(nums) == 0:
            return nums

        permutaions = []
        self.helper(nums, [], permutaions)
        print(permutaions)

    # 递归定义，把以permutation开头的的所有排列放到permutations里
    def helper(self, nums, permutation, permutations):
        if len(permutation) == len(nums):
            permutations.append(list(permutation))
            return

        # 递归的拆解
        for i in range(len(nums)):
            if nums[i] in permutation:
                continue

            permutation.append(nums[i])
            self.helper(nums, permutation, permutations)
            permutation.pop()

solution = Solution()
solution.permutations([1, 2, 3])