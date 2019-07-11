#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/11 2:32 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 20. Valid Parentheses.py
# @Software: IntelliJ IDEA


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peak(self):
        return self.stack[-1]

    def get_len(self):
        return len(self.stack)

class Solution:
    """
    ()[]{}
    """
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        stack = Stack()
        i = 0
        while i < len(s):
            cur = s[i]
            if cur == ')':
                if stack.get_len() == 0 or stack.pop() != '(':
                    return False
            elif cur == ']':
                if stack.get_len() == 0 or stack.pop() != '[':
                    return False
            elif cur == '}':
                if stack.get_len() == 0 or stack.pop() != '{':
                    return False
            else:
                stack.push(cur)
            i += 1
        if stack.get_len():
            return False
        return True

    def isValid2(self, s: str) -> bool:
        d = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for c in s:
            if c in d:
                stack.append(c)
            elif stack and d[stack.pop()] == c:
                continue
            else:
                return False
        # if stack:
        #     return False
        # return True
        return stack == []


solution = Solution()
res = solution.isValid2("]")
print(res)
