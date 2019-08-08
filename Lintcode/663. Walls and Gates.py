#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/7 10:52 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 663. Walls and Gates.py
# @Software: IntelliJ IDEA


from collections import deque
class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def wallsAndGates(self, rooms):
        if rooms is None:
            return None

        m = len(rooms)
        if m == 0:
            return None

        n = len(rooms[0])
        if n == 0:
            return None

        queue = deque()
        visited = set()
        # assume there is a super starter point
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        while queue:
            curr = queue.popleft()

            for x, y in [[0, 1], [0, -1], [-1, 0], [1, 0]]:
                _x, _y = x + curr[0], y + curr[1]
                if not self.is_valid_position(rooms, _x, _y):
                    continue
                queue.append((_x, _y))
                rooms[_x][_y] = rooms[curr[0]][curr[1]] + 1


    def is_valid_position(self, rooms, i, j):
        return 0 <= i < len(rooms) and 0 <= j < len(rooms[0]) and rooms[i][j] == 2147483647


rooms = [
    [2147483647,-1,0,2147483647],
    [2147483647,2147483647,2147483647,-1],
    [2147483647,-1,2147483647,-1],
    [0,-1,2147483647,2147483647]]