#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/13 9:00 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : nqueens.py
# @Software: IntelliJ IDEA

class Solution:
    """
    @param: n: The number of queens
    @return: All distinct solutions
    """
    # transform n-queens problem to permutation problem
    def solveNQueens(self, n):
        if n <= 0:
            return n
        results = []
        self.search(n, [], results)
        print(results)

    def search(self, n, cols, results):
        row = len(cols)

        if row == n:
            results.append(self.to_format(cols))
            return

        for col in range(n):
            # if it does not meet the conditions
            if not self.is_valid(row, col, cols):
                continue

            cols.append(col)
            self.search(n, cols, results)
            cols.pop()

    def to_format(self, cols):
        n = len(cols)
        result = []
        for i in range(n):
            result.append("".join(["Q" if j == cols[i] else "." for j in range(n)]))
        return result

    def is_valid(self, row, col, cols):
        for r, c in enumerate(cols):
            # if there is column equal to current column
            if c == col:
                return False
            # two positions is in diagonal
            if r + c == row + col or r - c == row - col:
                return False
        return True


solution = Solution()
solution.solveNQueens(4)