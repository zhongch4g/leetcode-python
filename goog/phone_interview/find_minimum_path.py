#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/7 8:52 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : find_minimum_path.py
# @Software: IntelliJ IDEA


"""
给一个matrix，有0 1 -1，从[0][0]这个点开始，找到-1的路径，要求返回一条最短路径，-1的位置可能在任何位置,每次可以走8个方向
"""
from collections import deque
class Solution:
    def find_minimum_path(self, mat):
        if not mat or not mat[0]:
            return []
        m = len(mat)
        n = len(mat[0])

        visited = {(0, 0)}
        cur_to_father = {}
        queue = deque([(0, 0)])
        destination = None
        while queue:
            i, j = queue.popleft()
            if mat[i][j] == -1:
                destination = (i, j)
                break

            # 8 direction
            for _x, _y in [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (1, -1), (-1, 1)]:
                x = i + _x
                y = j + _y
                if x < 0 or x >= m or y < 0 or y >= n:
                    continue
                if (x, y) in visited:
                    continue
                if mat[x][y] == 0:
                    continue
                queue.append((x, y))
                visited.add((x, y))
                cur_to_father[(x, y)] = (i, j)

        if not destination:
            return []
        result = [destination]
        while destination in cur_to_father:
            result.append(cur_to_father[destination])
            destination = cur_to_father[destination]
        print(result[::-1])
        return result[::-1]


matrix = [[1,0,0,1],
          [0,1,1,0],
          [1,-1,0,1]]

solution = Solution()
solution.find_minimum_path(matrix)