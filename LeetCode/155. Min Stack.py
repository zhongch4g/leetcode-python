#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 8:44 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 155. Min Stack.py
# @Software: IntelliJ IDEA

import sys
class Node:
    def __init__(self, value, MIN):
        self.value = value
        self.MIN = MIN
        self.next = None

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.dummy = Node(0, sys.maxsize)

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if not self.dummy.next:
            self.dummy.next = Node(x, x)
        else:
            new_node = Node(x, min(x, self.dummy.next.MIN))
            new_node.next = self.dummy.next
            self.dummy.next = new_node

    def pop(self):
        """
        :rtype: None
        """
        if not self.dummy.next:
            return -1
        self.dummy = self.dummy.next


    def top(self):
        """
        :rtype: int
        """
        if not self.dummy.next:
            return -1
        return self.dummy.next.value


    def getMin(self):
        """
        :rtype: int
        """
        if not self.dummy.next:
            return -1
        return self.dummy.next.MIN


        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()


obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)