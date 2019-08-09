#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 7:01 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 573. Build Post Office II.py
# @Software: IntelliJ IDEA

import sys
from collections import deque
class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """
    # 超时
    def shortestDistance(self, grid):
        if grid is None:
            return -1

        m = len(grid)
        if m == 0:
            return -1
        n = len(grid[0])
        if n == 0:
            return -1
        house_num = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    house_num += 1

        min_step = sys.maxsize
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    step, curr_house = self.bfs(grid, i, j)
                    if curr_house == house_num:
                        min_step = min(min_step, step)
        if min_step == sys.maxsize:
            return -1
        return min_step

    def bfs(self, grid, x, y):
        queue = deque([(x, y)])
        visited = {(x, y)}
        path_sum = 0
        curr_house = 0
        step = 0
        while queue:

            for i in range(len(queue)):
                curr_i, curr_j = queue.popleft()

                if grid[curr_i][curr_j] == 1:
                    path_sum += step
                    curr_house += 1
                    continue

                for i, j in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    _x, _y = curr_i + i, curr_j + j
                    if not self.is_valid(grid, _x, _y):
                        continue
                    if (_x, _y) in visited:
                        continue
                    queue.append((_x, _y))
                    visited.add((_x, _y))
            step += 1
        return path_sum, curr_house

    def is_valid(self, grid, x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != 2


    def shortestDistance2(self, grid):
        if grid is None:
            return -1

        m = len(grid)
        if m == 0:
            return -1
        n = len(grid[0])
        if n == 0:
            return -1
        house_num = 0

        house_to_groud = [[sys.maxsize] * n for i in range(m)]
        groud_to_house = [[0] * n for i in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.bfs1(grid, i, j, house_to_groud, groud_to_house)
                    house_num += 1
        min_dis = sys.maxsize
        print(groud_to_house)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and groud_to_house[i][j] == house_num:
                    min_dis = min(min_dis, house_to_groud[i][j])
        return -1 if min_dis == sys.maxsize else min_dis

    def bfs1(self, grid, i, j, house_to_groud, groud_to_house):

        queue = deque([(i, j)])
        visited = {(i, j)}
        step = 0
        while queue:

            for i in range(len(queue)):
                curr_i, curr_j = queue.popleft()
                if house_to_groud[curr_i][curr_j] == sys.maxsize:
                    house_to_groud[curr_i][curr_j] = 0
                house_to_groud[curr_i][curr_j] += step

                for i, j in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                    _x, _y = curr_i + i, curr_j + j
                    if not self.is_valid1(grid, _x, _y):
                        continue
                    if (_x, _y) in visited:
                        continue
                    queue.append((_x, _y))
                    visited.add((_x, _y))
                    groud_to_house[_x][_y] += 1

            step += 1

    def is_valid1(self, grid, x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == 0

solution = Solution()
res = solution.shortestDistance2([[0,1,0,0,0],
                                 [1,0,0,2,1],
                                 [0,1,0,0,0]])
print(res)