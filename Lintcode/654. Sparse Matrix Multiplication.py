#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/27 8:38 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 654. Sparse Matrix Multiplication.py
# @Software: IntelliJ IDEA


class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):

        row_vectors = self.convert_to_row_vector(A)
        col_vectors = self.convert_to_col_vector(B)
        matrix = []
        for row_vector in row_vectors:
            row = []
            for col_vector in col_vectors:
                row.append(self.muti_vector(row_vector, col_vector))
            matrix.append(row)
        return matrix

    def muti_vector(self, v1, v2):
        i, j = 0, 0
        res = 0
        while i < len(v1) and j < len(v2):
            if v1[i][0] < v2[j][0]:
                i += 1
            elif v1[i][0] > v2[j][0]:
                j += 1
            else:
                res += v1[i][1] * v2[j][1]
                i += 1
                j += 1
        return res

    def convert_to_row_vector(self, matrix):
        vectors = []
        for row in matrix:
            vector = []
            for idx, col in enumerate(row):
                if col == 0:
                    continue
                vector.append((idx, col))
            vectors.append(vector)
        return vectors

    def convert_to_col_vector(self, matrix):
        m, n = len(matrix), len(matrix[0])
        vectors = []
        for col in range(n):
            vector = []
            for row in range(m):
                if matrix[row][col] == 0:
                    continue
                vector.append((row, matrix[row][col]))
            vectors.append(vector)
        return vectors



A = [[1,0,0],
     [-1,0,3]]
B = [[7,0,0],
     [0,0,0],
     [0,0,1]]

solution = Solution()
solution.multiply(A, B)
