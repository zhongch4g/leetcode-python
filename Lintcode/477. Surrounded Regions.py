#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 12:14 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 477. Surrounded Regions.py
# @Software: IntelliJ IDEA


from collections import deque
class Solution:
    """
    @param: board: board a 2D board containing 'X' and 'O'
    @return: nothing
    """
    def surroundedRegions(self, board):

        if board is None:
            return None

        m = len(board)
        if m == 0:
            return None

        n = len(board[0])
        if n == 0:
            return None

        queue = deque()

        # first row and last row
        for i in range(n):
            if board[0][i] == 'O':
                queue.append((0, i))
                board[0][i] = 'V'
            if board[m - 1][i] == 'O':
                queue.append((m - 1, i))
                board[m - 1][i] = 'V'
        for j in range(m):
            if board[j][0] == 'O':
                queue.append((j, 0))
                board[j][0] = 'V'
            if board[j][n - 1] == 'O':
                queue.append((j, n - 1))
                board[j][n - 1] = 'V'

        while queue:
            curr = queue.popleft()
            for x, y in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
                _x, _y = x + curr[0], y + curr[1]
                if not self.is_valid_position(board, _x, _y):
                    continue
                board[_x][_y] = 'V'
                queue.append((_x, _y))

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'V':
                    board[i][j] = 'O'

    def is_valid_position(self, grid, i, j):
        return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 'O'
