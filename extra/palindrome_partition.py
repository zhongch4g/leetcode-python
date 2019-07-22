#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/4 3:55 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : palindrome_partition.py
# @Software: IntelliJ IDEA


class Solution():
    def partition(self, s):
        results = []
        self.dfs(s, [], results)
        return results

    def dfs(self, s, stringlist, results):
        if len(s) == 0:
            results.append(list(stringlist))
            return

        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if self.is_palindrome(prefix):
                stringlist.append(prefix)
                self.dfs(s[i:], stringlist, results)
                stringlist.pop()

    def is_palindrome(self, str):
        return str == str[::-1]



solution = Solution()
results = solution.partition('aba')
print(results)