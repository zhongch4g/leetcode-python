#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/13 7:48 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 986. Interval List Intersections.py
# @Software: IntelliJ IDEA



class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            if A[i][1] < B[j][0]:
                i += 1
            elif A[i][0] > B[j][1]:
                j += 1
            else:
                result.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])])
                if A[i][1] < B[j][1]:
                    i += 1
                else:
                    j += 1
        return result