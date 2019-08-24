#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 9:49 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 289. Game of Life.py
# @Software: IntelliJ IDEA


class Solution:
    def gameOfLife(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #  live (1) or dead (0)

        m = len(board)
        if m == 0:
            return board
        n = len(board[0])
        if n == 0:
            return board

        copy_board = [[board[i][j] for j in range(n)] for i in range(m)]
        print(copy_board)
        for i in range(m):
            for j in range(n):
                neighbors = self.count_neighbors(copy_board, i, j)
                if copy_board[i][j] == 0 and neighbors == 3:
                    board[i][j] = 1
                if copy_board[i][j] == 1 and neighbors not in [2, 3]:
                    board[i][j] = 0

    def count_neighbors(self, board, i, j):
        count = 0
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)]:
            _x, _y = i + x, j + y
            if _x < 0 or _x >= len(board) or _y < 0 or _y >= len(board[0]):
                continue
            if board[_x][_y] == 1:
                count += 1
        return count


# Fellow up 1: no extra space
class Solution2:
    def gameOfLife(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #  live (1) or dead (0)

        m = len(board)
        if m == 0:
            return board
        n = len(board[0])
        if n == 0:
            return board
        # 1 -> 0 -1   0 -> 1 2
        for i in range(m):
            for j in range(n):
                neighbors = self.count_neighbors(board, i, j)
                if board[i][j] == 0 and neighbors == 3:
                    board[i][j] = 2
                if board[i][j] == 1 and neighbors not in [2, 3]:
                    board[i][j] = -1

        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0

    def count_neighbors(self, board, i, j):
        count = 0
        for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (-1, 1), (1, 1), (1, -1)]:
            _x, _y = i + x, j + y
            if _x < 0 or _x >= len(board) or _y < 0 or _y >= len(board[0]):
                continue
            if abs(board[_x][_y]) == 1:
                count += 1
        return count

import collections
class Solution3:
    def gameOfLifeInfinite(self, live):
        ctr = collections.Counter((I, J)
                                  for i, j in live
                                  for I in range(i-1, i+2)
                                  for J in range(j-1, j+2)
                                  if I != i or J != j)
        return {ij
                for ij in ctr
                if ctr[ij] == 3 or ctr[ij] == 2 and ij in live}

    def gameOfLife(self, board):
        live = {(i, j) for i, row in enumerate(board) for j, live in enumerate(row) if live}
        live = self.gameOfLifeInfinite(live)
        for i, row in enumerate(board):
            for j in range(len(row)):
                row[j] = int((i, j) in live)
        print(board)

board = [[0,1,0],
         [0,0,1],
         [1,1,1],
         [0,0,0]]
solution = Solution3()
solution.gameOfLife(board)