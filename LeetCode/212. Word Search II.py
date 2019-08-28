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


class Solution2:
    def findWords(self, board, words):
        m = len(board)
        if m == 0:
            return []
        n = len(board[0])
        if n == 0:
            return []
        if not words:
            return []

        trie = {}
        for word in words:
            root = trie
            for c in word:
                if c not in root:
                    root[c] = {}
                root = root[c]
            root['#'] = word
        results = set()
        for i in range(m):
            for j in range(n):
                if board[i][j] not in trie:
                    continue
                self.search(board, i, j, trie[board[i][j]], {(i, j)}, results)
        return results

    def search(self, board, i, j, trie, visited, results):

        if '#' in trie:
            results.add(trie['#'])
            trie.pop('#')

        for s1, s2 in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            _x = i + s1
            _y = j + s2
            if _x < 0 or _x >= len(board) or _y < 0 or _y >= len(board[0]):
                continue
            if (_x, _y) in visited:
                continue
            visited.add((_x, _y))
            if board[_x][_y] in trie:
                self.search(board, _x, _y, trie[board[_x][_y]], visited, results)
            visited.remove((_x, _y))


board = [
    ['o','a','a','n'],
    ['e','t','a','e'],
    ['i','h','k','r'],
    ['i','f','l','v']
]
board1 = [["b"],
          ["a"],
          ["b"],
          ["b"],
          ["a"]]
words = ["baa","abba","baab","aba"]
solution = Solution2()
res = solution.findWords(board1, words)
print(res)
