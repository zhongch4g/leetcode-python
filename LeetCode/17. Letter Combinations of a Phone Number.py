#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/11 10:55 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 17. Letter Combinations of a Phone Number.py
# @Software: IntelliJ IDEA


class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []

        dic = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
               '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        combinations = []
        self.search(digits, 0, '', combinations, dic)
        print(combinations)

    def search(self, digits, index, combination, combinations, dic):
        # base case :
        if len(digits) == len(combination):
            combinations.append(combination)
            return

        if len(digits) <= index:
            return

        for c in dic[digits[index]]:
            self.search(digits, index + 1, combination + c, combinations, dic)


solution = Solution()
solution.letterCombinations('23')