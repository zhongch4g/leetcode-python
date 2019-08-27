#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/27 3:27 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 591. Connecting Graph III.py
# @Software: IntelliJ IDEA


class ConnectingGraph3:
    """
    @param a: An integer
    @param b: An integer
    @return: nothing
    """
    def __init__(self, n):
        self.father = []
        for i in range(n + 1):
            self.father.append(i)
        self.number = n

    def connect(self, a, b):
        # write your code here
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.number -= 1


    """
    @return: An integer
    """
    def query(self):
        # write your code here
        return self.number

    def find(self, key):
        if self.father[key] == key:
            return key
        self.father[key] = self.find(self.father[key])
        return self.father[key]