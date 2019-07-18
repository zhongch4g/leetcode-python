#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/17 10:13 PM
# @Author  : zhongch4g
# @Site    :
# @File    : 79. Word Search.py
# @Software: IntelliJ IDEA


x = [1, -1, 0, 0]
y = [0, 0, 1, -1]
class Solution:
    def exist(self, board, word):
        if word == '':
            return False
        if not board or not board[0]:
            if word == '':
                return True
            return False

        m, n = len(board), len(board[0])
        visited = [[False for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if board[i][j] != word[0]:
                    continue
                if self.search(board, i, j, word, 0):
                    return True
        return False


    def search(self, board, i, j, word, index):

        if index == len(word):
            return True

        if not self.in_board(board, i, j):
            return False

        if board[i][j] != word[index]:
            return False


        stuck, board[i][j] = board[i][j], '#'

        result = self.search(board, i-1, j, word, index + 1) or \
                 self.search(board, i, j-1, word, index + 1) or \
                 self.search(board, i+1, j, word, index + 1) or \
                 self.search(board, i, j+1, word, index + 1)
        board[i][j] = stuck
        return result

    def in_board(self, board, i, j):
        return 0 <= i < len(board) and 0 <= j < len(board[0])


board =[
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]
board1 = [["A","B","C","E"],
          ["S","F","C","S"],
          ["A","D","E","E"]]
solution = Solution()
res = solution.exist(board, "ABCCED")
print(res)