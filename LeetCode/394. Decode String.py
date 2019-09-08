#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/8 5:12 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 394. Decode String.py
# @Software: IntelliJ IDEA


class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return ""

        stack = []
        i = 0
        while i < len(s):
            if s[i] != ']':
                stack.append(s[i])
                i += 1
                continue

            # s[i] == ']'
            # note string
            string = ''
            while stack and 'A' <= stack[-1] <= 'Z' or 'a' <= stack[-1] <= 'z':
                string = stack.pop() + string
            # pop '['
            if stack[-1] == '[':
                stack.pop()
            # note number
            number = ""
            while stack and '0' <= stack[-1] <= '9':
                number = stack.pop() + number

            if number:
                number = int(number)
                stack.append(number * string)
            else:
                stack.append(string)

            i += 1

        return "".join(stack)