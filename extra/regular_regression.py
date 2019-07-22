#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/4 9:20 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : regular_regression.py
# @Software: IntelliJ IDEA

class Solution:
    """
    @param s: A string
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        return self.is_match_regrex(s, 0, p, 0, {})

    # return can match or not
    def is_match_regrex(self, source, i, parttern, j, memo):
        if (i, j) in memo:
            return memo[(i, j)]

        if len(source) == i:
            return self.is_empty(parttern[j:])

        if len(parttern) == j:
            return False

        if j < len(parttern) - 1 and parttern[j + 1] == "*":
            matched = self.is_single_match(source[i], parttern[j]) \
                      and self.is_match_regrex(source, i + 1, parttern, j, memo) \
                      or self.is_match_regrex(source, i, parttern, j + 2, memo)
        else:
            matched = self.is_single_match(source[i], parttern[j]) \
                   and self.is_match_regrex(source, i + 1, parttern, j + 1, memo)

        memo[(i, j)] = matched
        return matched

    def is_single_match(self, source, parttern):
        return source == parttern or parttern == "."

    def is_empty(self, parttern):
        if len(parttern) % 2 == 1:
            return False

        #需要满足"x*x*"的形式
        for i in range(len(parttern) // 2):
            if parttern[i * 2 + 1] != '*':
                return False
        return True

solution = Solution()
result = solution.isMatch("bbbbbbbbbbb", "a*b")
print(result)