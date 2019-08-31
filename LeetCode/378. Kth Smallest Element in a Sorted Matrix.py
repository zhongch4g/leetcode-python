#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/30 10:25 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 378. Kth Smallest Element in a Sorted Matrix.py
# @Software: IntelliJ IDEA


import heapq
class Pair:
    def __init__(self, x, y, val):
        self.x = x
        self.y = y
        self.val = val

    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        if not matrix:
            return 0

        heap = [(matrix[0][0], 0, 0)]
        visited = {(0, 0)}
        for _ in range(k - 1):
            val, px, py = heapq.heappop(heap)
            for _x, _y in [(0, 1), (1, 0)]:
                nx = px + _x
                ny = py + _y
                if nx < 0 or nx >= len(matrix) or ny < 0 or ny >= len(matrix[0]):
                    continue
                if (nx, ny) in visited:
                    continue
                heapq.heappush(heap, (matrix[nx][ny], nx, ny))
                visited.add((nx, ny))
        return heapq.heappop(heap)[0]
