#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/4 5:19 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 216. Combination Sum III.py
# @Software: IntelliJ IDEA


class Solution:
    def combinationSum3(self, k: int, n: int):

        combinations = []

        self.search(k, n, 1, [], combinations)
        return combinations


    def search(self, k, n, index, combination, combinations):

        if k == 0 and n == 0:
            combinations.append(list(combination))
            return

        for i in range(index, 10):
            if i > n:
                return

            combination.append(i)
            self.search(k - 1, n - i, i + 1, combination, combinations)
            combination.pop()