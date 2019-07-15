#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/14 8:26 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 48. Rotate Image.py
# @Software: IntelliJ IDEA


class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        # reflect in vertical
        matrix.reverse()
        # reflect in diagonal
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        print(matrix)


matrix = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
         ]
"""
goal:
[[7,4,1]
 [8,5,2]
 [9,6,3]]
"""
solution = Solution()
solution.rotate(matrix)