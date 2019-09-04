#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/4 4:38 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 40. Combination Sum II.py
# @Software: IntelliJ IDEA


class Solution:
    def combinationSum2(self, candidates, target: int):
        if not candidates:
            return []
        candidates.sort()
        combinations = []

        self.search(candidates, 0, target, [], combinations, set())
        return combinations

    def search(self, candidates, index, target, combination, combinations, visited):

        if target == 0:
            combinations.append(list(combination))
            return

        for i in range(index, len(candidates)):
            if target < candidates[i]:
                return

            if i > 0 and candidates[i] == candidates[i - 1] and i - 1 not in visited:
                continue

            combination.append(candidates[i])
            visited.add(i)
            self.search(candidates, i + 1, target - candidates[i], combination, combinations, visited)
            visited.remove(i)
            combination.pop()