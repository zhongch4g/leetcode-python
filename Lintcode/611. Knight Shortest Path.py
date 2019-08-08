#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/8 6:28 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 611. Knight Shortest Path.py
# @Software: IntelliJ IDEA

class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


from collections import deque
class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    """
    def shortestPath(self, grid, source, destination):

        if grid is None:
            return -1

        m = len(grid)
        if m == 0:
            return -1
        n = len(grid[0])
        if n == 0:
            return -1

        queue = deque([(source.x, source.y)])
        distance = {(source.x, source.y): 0}

        while queue:

            for i in range(len(queue)):
                x, y = queue.popleft()
                if (x, y) == (destination.x, destination.y):
                    return distance[(x, y)]
                for i, j in [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]:
                    _x, _y = x + i, y + j
                    if not self.is_valid_position(grid, _x, _y):
                        continue
                    if (_x, _y) in distance:
                        continue
                    queue.append((_x, _y))
                    distance[(_x, _y)] = distance[(x, y)] + 1
        return -1

    def is_valid_position(self, grid, i, j):
        return 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] != 1

grid =  [[0,0,0],
         [0,0,0],
         [0,0,0]]
source = [2, 0]
destination = [2, 2]
