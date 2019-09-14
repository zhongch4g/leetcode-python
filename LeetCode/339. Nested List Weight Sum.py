#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/13 6:52 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 339. Nested List Weight Sum.py
# @Software: IntelliJ IDEA


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        stack = []
        for ele in nestedList:
            stack.append((ele, 1))
        sum = 0
        while stack:
            element, depth = stack.pop()
            if element.isInteger():
                sum += depth * element.getInteger()
            else:
                for e in element.getList():
                    stack.append((e, depth + 1))
        return sum

