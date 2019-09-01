#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/17 10:53 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 1162. As Far from Land as Possible .py
# @Software: IntelliJ IDEA


import sys
from collections import deque
class Solution:
    def maxDistance(self, grid) -> int:

        # 0 water and 1 land

        # check if all is water or all is land

        m = len(grid)
        if m == 0:
            return -1
        n = len(grid[0])
        if n == 0:
            return -1
        w, l = 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    w += 1
                if grid[i][j] == 1:
                    l += 1
        if w == 0 or l == 0:
            return -1

        queue = deque([])
        d = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))

        while queue:

            size = len(queue)
            for i in range(size):
                p, q = queue.popleft()

                for i1, i2 in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    _x, _y = p + i1, q + i2
                    if self.is_valid(grid, _x, _y) and grid[_x][_y] == 0:
                        queue.append((_x, _y))
                        grid[_x][_y] = 1
            d += 1

        return d - 1

    def is_valid(self, grid, i, j):
        return 0 <= i < len(grid) and 0 <= j < len(grid[0])


grid = [[1,0,0],[0,0,0],[0,0,0]]
solution = Solution()
res = solution.maxDistance(grid)
print(res)

