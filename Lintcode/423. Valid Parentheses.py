#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 3:05 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 423. Valid Parentheses.py
# @Software: IntelliJ IDEA


class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        if not s:
            return True

        stack = []
        for bracket in s:
            if not stack or bracket in ['(', '{', '[']:
                stack.append(bracket)
                continue

            if stack and bracket == ']':
                cur = stack.pop()
                if cur != '[':
                    return False
            elif stack and bracket == '}':
                cur = stack.pop()
                if cur != '{':
                    return False
            elif stack and bracket == ')':
                cur = stack.pop()
                if cur != '(':
                    return False
        if not stack:
            return True
        return False