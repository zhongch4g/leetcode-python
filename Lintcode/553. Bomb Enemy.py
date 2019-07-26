#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/24 10:22 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 553. Bomb Enemy.py
# @Software: IntelliJ IDEA


class Solution:
    """
    @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """
    def maxKilledEnemies(self, grid):
        m = len(grid)
        if m == 0:
            return 0

        n = len(grid[0])
        if n == 0:
            return 0

        up = [[0] * n for i in range(m)]
        down = [[0] * n for i in range(m)]
        left = [[0] * n for i in range(m)]
        right = [[0] * n for i in range(m)]

        # up
        for i in range(m):
            for j in range(n):
                if 'W' == grid[i][j]:
                    continue

                if 'E' == grid[i][j]:
                    up[i][j] = 1

                if i > 0:
                    up[i][j] += up[i-1][j]

        # down
        for i in range(m-1, -1, -1):
            for j in range(n):
                if 'W' == grid[i][j]:
                    continue

                if 'E' == grid[i][j]:
                    down[i][j] = 1

                if i < m - 1:
                    down[i][j] += down[i+1][j]

        # left
        for i in range(m):
            for j in range(n):
                if 'W' == grid[i][j]:
                    continue

                if 'E' == grid[i][j]:
                    left[i][j] = 1

                if j > 0:
                    left[i][j] += left[i][j-1]

        # right
        for i in range(m):
            for j in range(n-1, -1, -1):
                if 'W' == grid[i][j]:
                    continue

                if 'E' == grid[i][j]:
                    right[i][j] = 1

                if j < n - 1:
                    right[i][j] += right[i][j+1]

        res = [[0] * n for i in range(m)]
        result = 0
        for i in range(m):
            for j in range(n):
                if '0' == grid[i][j]:
                    res[i][j] = up[i][j] + down[i][j] + left[i][j] + right[i][j]
                    result = max(result, res[i][j])
        return result