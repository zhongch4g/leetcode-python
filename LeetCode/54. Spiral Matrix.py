#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/25 6:52 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 54. Spiral Matrix.py
# @Software: IntelliJ IDEA


class Solution:
    def spiralOrder(self, matrix):
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        if n == 0:
            return []
        up = 0
        down = m - 1
        left = 0
        right = n - 1

        results = []
        while up <= down and left <= right:
            # up
            for n in range(left, right + 1):
                results.append(matrix[up][n])
            up += 1

            if up > down or left > right:
                break
            # right
            for n in range(up, down + 1):
                results.append(matrix[n][right])
            right -= 1

            if up > down or left > right:
                break
            # down
            for n in reversed(range(left, right + 1)):
                results.append(matrix[down][n])
            down -= 1

            if up > down or left > right:
                break
            # left
            for n in reversed(range(up, down + 1)):
                results.append(matrix[n][left])
            left += 1
        return results


solution = Solution()
solution.spiralOrder([[1, 2, 3, 4],[5, 6, 7, 8],[9,10,11,12]])