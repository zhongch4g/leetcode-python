#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/29 4:39 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 12. Min Stack.py
# @Software: IntelliJ IDEA


class MinStack:

    def __init__(self):
        # do intialization if necessary
        self.stack = []

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        # write your code here
        if not self.stack:
            self.stack.append((number, number))
        else:
            peak = self.stack[-1]
            if number > peak[1]:
                self.stack.append((number, peak[1]))
            else:
                self.stack.append((number, number))


    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        return self.stack.pop()[0]

    """
    @return: An integer
    """
    def min(self):
        return self.stack[-1][1]