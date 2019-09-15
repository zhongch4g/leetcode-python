#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/14 11:54 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 1190. Reverse Substrings Between Each Pair of Parentheses.py
# @Software: IntelliJ IDEA


class Solution(object):
    def reverseParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """

        if not s:
            return s

        stack = []
        helper_stack = []

        for c in s:
            if c != ")":
                stack.append(c)
                continue

            # reverse
            while stack and stack[-1] != '(':
                helper_stack.append(stack.pop())

            if stack and stack[-1] == '(':
                stack.pop()

            while helper_stack:
                stack.append(helper_stack.pop(0))

        return "".join(stack)