#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 8:25 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 973. K Closest Points to Origin.py
# @Software: IntelliJ IDEA


import heapq, math

class Solution:
    def kClosest(self, points, K: int):

        heap = []
        for x, y in points:
            distance = math.sqrt(x ** 2 + y ** 2)
            if len(heap) == K:
                heapq.heappushpop(heap, (-distance, (x, y)))
            else:
                heapq.heappush(heap, (-distance, (x, y)))

        return [t[1] for t in heap]