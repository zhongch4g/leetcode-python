#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 10:11 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 778. Pacific Atlantic Water Flow.py
# @Software: IntelliJ IDEA

import sys
from collections import deque
class Solution:
    """
    @param matrix: the given matrix
    @return: The list of grid coordinates
    """
    def pacificAtlantic(self, matrix):

        if matrix is None:
            return -1

        m = len(matrix)
        if m == 0:
            return -1
        n = len(matrix[0])
        if n == 0:
            return -1

        pacific = set()
        atlantic = set()

        for i in range(m):
            self.bfs(matrix, i, 0, pacific)
            self.bfs(matrix, i, n - 1, atlantic)
        for j in range(n):
            self.bfs(matrix, 0, j, pacific)
            self.bfs(matrix, m - 1, j, atlantic)
        return list(pacific & atlantic)


    def bfs(self, matrix, x, y, visited):

        queue = deque([(x, y)])
        visited.add((x, y))
        while queue:
            curr_i, curr_j = queue.popleft()
            for i, j in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                _x, _y = curr_i + i, curr_j + j
                if not self.is_valid(matrix, _x, _y):
                    continue
                if (_x, _y) in visited or matrix[_x][_y] < matrix[curr_i][curr_j]:
                    continue

                queue.append((_x, _y))
                visited.add((_x, _y))

    def is_valid(self, matrix, x, y):
        return 0 <= x < len(matrix) and 0 <= y < len(matrix[0])




matrix = [[1,2,2,3,5],
         [3,2,3,4,4],
         [2,4,5,3,1],
         [6,7,1,4,5],
         [5,1,1,2,4]]
solution = Solution()
res = solution.pacificAtlantic(matrix)
print(res)
