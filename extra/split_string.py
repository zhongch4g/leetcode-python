#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/4 9:04 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : split_string.py
# @Software: IntelliJ IDEA

class Solution:
    """
    @param: : a string to be split
    @return: all possible split string array
    """

    def splitString(self, s):
        results = []
        self.dfs(s, [], results)
        return results

    def dfs(self, s, stringlist, results):
        if len(s) == 0:
            results.append(list(stringlist))
            return

        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if len(prefix) <= 2:
                stringlist.append(prefix)
                self.dfs(s[i:], stringlist, results)
                stringlist.pop()


solution = Solution()
results = solution.splitString("123")
print(results)