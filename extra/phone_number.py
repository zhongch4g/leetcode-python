#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/13 11:00 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : phone_number.py
# @Software: IntelliJ IDEA

class Solution:
    MAPPING = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def letterCombinations(self, digits):
        if not digits:
            return digits

        results = []
        self.dfs(digits, 0, "", results)
        return results

    def dfs(self, digits, index, string, results):
        if index == len(digits):
            results.append(string)
            return

        for i in Solution.MAPPING[digits[index]]:
            self.dfs(digits, index + 1, string + i, results)