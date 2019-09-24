#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/23 10:00 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 361. Bomb Enemy.py
# @Software: IntelliJ IDEA


import sys
class Solution:
    def maxKilledEnemies(self, grid) -> int:
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
        # count up
        for i in range(m):
            for j in range(n):
                if i == 0:
                    up[i][j] = 1 if grid[i][j] == 'E' else 0
                    continue
                if grid[i][j] == 'W':
                    up[i][j] = 0
                elif grid[i][j] == 'E':
                    up[i][j] = up[i - 1][j] + 1
                elif grid[i][j] == '0':
                    up[i][j] = up[i - 1][j]

        # count down
        for i in range(m - 1, -1, -1):
            for j in range(n):
                if i == m - 1:
                    down[i][j] = 1 if grid[i][j] == 'E' else 0
                    continue
                if grid[i][j] == 'W':
                    down[i][j] = 0
                elif grid[i][j] == 'E':
                    down[i][j] = down[i + 1][j] + 1
                elif grid[i][j] == '0':
                    down[i][j] = down[i + 1][j]

        # count left
        for i in range(m):
            for j in range(n):
                if j == 0:
                    left[i][j] = 1 if grid[i][j] == 'E' else 0
                    continue
                if grid[i][j] == 'W':
                    left[i][j] = 0
                elif grid[i][j] == 'E':
                    left[i][j] = left[i][j - 1] + 1
                elif grid[i][j] == '0':
                    left[i][j] = left[i][j - 1]

        # count right
        for i in range(m):
            for j in range(n - 1, -1, -1):
                if j == n - 1:
                    right[i][j] = 1 if grid[i][j] == 'E' else 0
                    continue
                if grid[i][j] == 'W':
                    right[i][j] = 0
                elif grid[i][j] == 'E':
                    right[i][j] = right[i][j + 1] + 1
                elif grid[i][j] == '0':
                    right[i][j] = right[i][j + 1]

        maximum = - sys.maxsize - 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    maximum = max(maximum, left[i][j] + right[i][j] + up[i][j] + down[i][j])
        return maximum if maximum != - sys.maxsize - 1 else 0