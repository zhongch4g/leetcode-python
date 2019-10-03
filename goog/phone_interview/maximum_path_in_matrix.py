#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/2 8:27 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : maximum_path_in_matrix.py
# @Software: IntelliJ IDEA

"""
给一个二维矩阵，每个元素都是非负整数。找到所有可能路径的最大的和。
在一条路径中，不能包含0，路径可以向上下左右延伸，每个元素只能访问一次。假设矩阵中正整数的路径不可能形成环。
"""
import sys
class Solution:
    def __init__(self):
        self.max_path = - sys.maxsize - 1

    def find_maximum_path(self, matrix):

        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != 0 and (i, j) not in visited:
                    self.helper(matrix, i, j, visited)
        print(self.max_path)

    def helper(self, matrix, i, j, visited):
        if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
            return 0
        if matrix[i][j] == 0 or (i, j) in visited:
            return 0
        visited.add((i, j))

        left = self.helper(matrix, i, j - 1, visited)
        right = self.helper(matrix, i, j + 1, visited)
        up = self.helper(matrix, i + 1, j, visited)
        down = self.helper(matrix, i - 1, j, visited)

        # add two longest single root
        four_path = [left, right, up, down]
        four_path.sort()
        cur_path = matrix[i][j] + four_path[2] + four_path[3]
        if cur_path > self.max_path:
            self.max_path = cur_path
        return matrix[i][j] + four_path[3]


matrix1 = [[5, 4, 1, 0], [1, 0, 1, 2], [3, 0, 0, 4], [0, 1, 2, 0]]
matrix2 = [[5, 4, 1, 3], [1, 0, 1, 0], [3, 0, 0, 4], [0, 1, 2, 0]]
solution = Solution()
# solution.find_maximum_path(matrix1)
solution.find_maximum_path(matrix2)


"""
Example 1:

Input:
5 4 1 0
1 0 1 2
3 0 0 4
0 1 2 0

Output: 21
Explanation: 3 -> 1 -> 5 -> 4 -> 1 -> 1 -> 2 -> 4
Example 2:

Input:
5 4 1 3
1 0 1 0
3 0 0 4
0 1 2 0

Output: 17
Explanation: 3 -> 1 -> 5 -> 4 -> 1 -> 3
"""