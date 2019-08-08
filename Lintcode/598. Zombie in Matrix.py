#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/7 11:28 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 598. Zombie in Matrix.py
# @Software: IntelliJ IDEA


from collections import deque
class Solution:
    """
    @param grid: a 2D integer grid
    @return: an integer
    """
    def zombie(self, grid):
        if grid is None:
            return None

        m = len(grid)
        if m == 0:
            return None

        n = len(grid[0])
        if n == 0:
            return None

        queue = deque()
        visited = set()
        # assume there is a super starter point
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
        step = -1
        while queue:
            step += 1
            for i in range(len(queue)):

                curr = queue.popleft()

                for x, y in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
                    _x, _y = x + curr[0], y + curr[1]
                    if not self.is_valid_position(grid, _x, _y):
                        continue
                    queue.append((_x, _y))
                    grid[_x][_y] = 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    return -1
        return step


    def is_valid_position(self, grid, i, j):
        return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 0


# 2 wall 1 zombie 0 people
grid = [[0,1,2,0,0],
        [1,0,0,2,1],
        [0,1,0,0,0]]
