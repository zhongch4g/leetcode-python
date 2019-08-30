#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/30 2:38 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 130. Surrounded Regions.py
# @Software: IntelliJ IDEA


from collections import deque
class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        m = len(board)
        if m == 0:
            return board
        n = len(board[0])
        if n == 0:
            return board

        queue = deque([])
        for i in range(m):
            if board[i][0] == 'O':
                board[i][0] = 'W'
                queue.append((i, 0))
            if board[i][n - 1] == 'O':
                board[i][n - 1] = 'W'
                queue.append((i, n - 1))

        for j in range(n):
            if board[0][j] == 'O':
                board[0][j] = 'W'
                queue.append((0, j))
            if board[m - 1][j] == 'O':
                board[m - 1][j] = 'W'
                queue.append((m - 1, j))

        while queue:
            x, y = queue.popleft()

            for p, q in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                _x = x + p
                _y = y + q
                if _x < 0 or _x >= m or _y <0 or _y >= n:
                    continue
                if board[_x][_y] != 'O':
                    continue
                board[_x][_y] = 'W'
                queue.append((_x, _y))
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'W':
                    board[i][j] = 'O'
