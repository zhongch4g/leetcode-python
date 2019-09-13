#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/13 5:16 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 341. Flatten Nested List Iterator.py
# @Software: IntelliJ IDEA


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
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
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.queue = deque([])
        self.nestedList = nestedList
        self.index = 0

    def next(self):
        """
        :rtype: int
        """

        return self.queue.popleft()


    def hasNext(self):
        """
        :rtype: bool
        """
        if not self.queue:
            while self.index < len(self.nestedList) and not self.queue:

                cur = self.nestedList[self.index]

                if cur.isInteger():
                    self.queue.append(cur.getInteger())
                else:
                    self.helper(cur.getList())

                self.index += 1

            if not self.queue:
                return False

        return True

    def helper(self, nested):

        for ele in nested:
            if ele.isInteger():
                self.queue.append(ele.getInteger())
            else:
                self.helper(ele.getList())



                # Your NestedIterator object will be instantiated and called as such:
                # i, v = NestedIterator(nestedList), []
                # while i.hasNext(): v.append(i.next())