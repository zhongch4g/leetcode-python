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


    # quick select

    def kClosest2(self, points, K: int):

        length =  len(points)
        l = 0
        r = length - 1
        while l <= r:
            mid = self.helper(points, l, r)
            if mid == K:
                break
            if mid < K:
                l = mid + 1
            else:
                r = mid - 1

        return points[:K]

    def helper(self, A, l, r):
        pivot = A[l]
        while (l < r):
            while l < r and self.compare(A[r], pivot) >= 0:
                r -= 1
            A[l] = A[r]
            while l < r and self.compare(A[l], pivot) <= 0:
                l += 1
            A[r] = A[l]
        A[l] = pivot
        return l

    def compare(self, p1, p2):
        return p1[0] * p1[0] + p1[1] * p1[1] - p2[0] * p2[0] - p2[1] * p2[1]
