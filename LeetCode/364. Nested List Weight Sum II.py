#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/13 7:42 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 364. Nested List Weight Sum II.py
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


from collections import deque
class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """

        prev = 0
        result = 0
        queue = deque([])
        for element in nestedList:
            queue.append(element)

        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                if cur.isInteger():
                    prev += cur.getInteger()
                else:
                    queue.extend(cur.getList())
            result += prev
        return result


