#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 3:09 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 10. Regular Expression Matching.py
# @Software: IntelliJ IDEA


class Solution:
    def isMatch(self, s, p):
        return self.search(s, 0, p, 0, {})

    def search(self, s, i, p, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == len(s):
            return self.isEmpty(p[j:])

        if j == len(p):
            return False

        if j < len(p) - 1 and p[j + 1] == "*":
            match = self.dotMatch(s, i, p, j) and self.search(s, i + 1, p, j, memo)\
                   or self.search(s, i, p, j + 2, memo)
        else:
            match = self.dotMatch(s, i, p, j) and self.search(s, i + 1, p, j + 1, memo)

        memo[(i, j)] = match
        return match

    def dotMatch(self, s, i, p, j):
        return s[i] == p[j] or p[j] == '.'

    def isEmpty(self, p):
        if len(p) % 2 == 1:
            return False
        #需要满足"x*x*"的形式
        for i in range(len(p) // 2):
            if p[i * 2 + 1] != '*':
                return False
        return True


s = "aab"
p = "c*a*b"
solution = Solution()
res = solution.isMatch(s, p)
print(res)
