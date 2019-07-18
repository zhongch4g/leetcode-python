#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/18 12:19 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 212. Word Search II.py
# @Software: IntelliJ IDEA


class Solution:
    def findWords(self, board, words):
        prefix = set()
        self.find_prefix(words, prefix)

        m, n = len(board), len(board[0])
        results = set()
        for i in range(m):
            for j in range(n):
                self.search(board, i, j, board[i][j], words, results, {(i, j)}, prefix)
        return results


    def find_prefix(self, words, prefix):
        for word in words:
            for i in range(len(word)):
                prefix.add(word[:i + 1])

    def search(self, board, i, j, word, words, results, visited, prefix):

        if word not in prefix:
            return

        if word in words:
            results.add(word)

        for step in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            _x, _y = i + step[0], j + step[1]

            if not self.is_over_board(board, _x, _y):
                continue
            if (_x, _y) in visited:
                continue

            visited.add((_x, _y))
            self.search(board, _x, _y, word + board[_x][_y], words, results, visited, prefix)
            visited.remove((_x, _y))


    def is_over_board(self, board, i, j):
        return 0 <= i < len(board) and 0 <= j < len(board[0])



board = [
    ['o','a','a','n'],
    ['e','t','a','e'],
    ['i','h','k','r'],
    ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
solution = Solution()
res = solution.findWords(board, words)
print(res)
