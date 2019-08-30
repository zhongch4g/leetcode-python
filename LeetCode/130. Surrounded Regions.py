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


# Union Find Solution
class Solution2:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or len(board) == 0:
            return

        m, n = len(board), len(board[0])

        dummy = m * n
        uf = UF(m, n)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    cvt = i * n + j
                    if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                        uf.union(cvt, dummy)
                        continue
                    for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nx = i + x
                        ny = j + y
                        if nx < 0 or nx >= m or ny < 0 or ny >= n or board[nx][ny] != 'O':
                            continue
                        neighbor = nx * n + ny
                        uf.union(neighbor, cvt)
        for i in range(m):
            for j in range(n):
                cid = i * n + j
                if board[i][j] == 'O' and uf.find(cid) != uf.find(dummy):
                    board[i][j] = 'X'

class UF:
    def __init__(self, m, n):
        self.father = [i for i in range(m * n + 1)]


    def union(self, id1, id2):
        root_id1 = self.find(id1)
        root_id2 = self.find(id2)
        if root_id1 != root_id2:
            self.father[root_id1] = root_id2

    def find(self, cid):
        if cid == self.father[cid]:
            return cid
        self.father[cid] = self.find(self.father[cid])
        return self.father[cid]
