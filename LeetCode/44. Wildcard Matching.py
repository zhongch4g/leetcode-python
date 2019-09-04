#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/4 6:56 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 44. Wildcard Matching.py
# @Software: IntelliJ IDEA


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == '' and p == '':
            return True

        return self.search(s, 0, p, 0, {})
    # idx1 开始的后缀能不能匹配idx2 开始的后缀
    def search(self, s, idx1, p, idx2, memo):
        if (idx1, idx2) in memo:
            return memo[(idx1, idx2)]
        if idx1 == len(s):
            if idx2 == len(p):
                return True
            else:
                return self.all_star(p[idx2:])

        if idx2 == len(p):
            return False

        if p[idx2] == '*':
            matched = self.search(s, idx1 + 1, p, idx2, memo) or self.search(s, idx1, p, idx2 + 1, memo)
        else:
            matched = self.is_single_match(s[idx1], p[idx2]) and self.search(s, idx1 + 1, p, idx2 + 1, memo)

        memo[(idx1, idx2)] = matched
        return matched


    def is_single_match(self, s, p):
        return s == p or p == '?'

    def all_star(self, s):
        for c in s:
            if c != '*':
                return False
        return True