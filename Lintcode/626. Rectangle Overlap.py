#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/23 5:02 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 626. Rectangle Overlap.py
# @Software: IntelliJ IDEA


"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param l1: top-left coordinate of first rectangle
    @param r1: bottom-right coordinate of first rectangle
    @param l2: top-left coordinate of second rectangle
    @param r2: bottom-right coordinate of second rectangle
    @return: true if they are overlap or false
    """
    def doOverlap(self, l1, r1, l2, r2):

        if l1.x > r2.x or l2.x > r1.x:
            return False

        if l1.y < r2.y or l2.y < r1.y:
            return False

        return True
