#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/14 12:16 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 39. Combination Sum.py
# @Software: IntelliJ IDEA


class Solution:
    def combinationSum(self, candidates, target):
        if not candidates:
            return []
        candidates.sort()

        combinations = []
        self.search(candidates, target, 0, [], combinations)
        return combinations

    def search(self, candidates, target, index, combination, combinations):
        # base case
        if target == 0:
            combinations.append(list(combination))
            return
        if target < 0:
            return
        if index >= len(candidates):
            return

        for i in range(index, len(candidates)):
            if candidates[i] > target:
                break
            combination.append(candidates[i])
            self.search(candidates, target - candidates[i], i, combination, combinations)
            combination.pop()


candidates = [2,3,6,7]
target = 8
solution = Solution()
solution.combinationSum(candidates, target)