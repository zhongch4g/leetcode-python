#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/20 1:10 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : word_search.py
# @Software: IntelliJ IDEA

class Solution:
    """
    @param board: A list of lists of character
    @param words: A list of string
    @return: A list of string
    """
    def wordSearchII(self, board, words):
        results = set()
        prefix = set()
        self.find_prefix(words, prefix)

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.search(i, j, board, words, board[i][j], results, set([(i, j)]), prefix)

        return list(results)

    def find_prefix(self, words, prefix):
        for word in words:
            for i in range(len(word)):
                prefix.add(word[:i + 1])

    def search(self, cur_x, cur_y, board, words, word, results, visited, prefix):
        if word not in prefix:
            return

        # 结果
        if word in words:
            results.add(word)
            # 不能加return 因为得到答案之后需要继续搜索
            # return

        for mov_x, mov_y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:

            _x, _y = cur_x + mov_x, cur_y + mov_y

            if not self.inside(board, _x, _y):
                continue

            if (_x, _y) in visited:
                continue

            visited.add((_x, _y))

            self.search(_x, _y, board, words, word + board[_x][_y],
                        results, visited, prefix)

            visited.remove((_x, _y))

    def inside(self, board, x, y):
        return 0 <= x < len(board) and 0 <= y < len(board[0])




# ["d o a f",
#  "a g a i",
#  "d c a n"]，["dog","dad","dgdg","can","again"]

solution = Solution()
board, words = ["abce","sfcs","adee"], ["see","se"]
solution.wordSearchII(board, words)