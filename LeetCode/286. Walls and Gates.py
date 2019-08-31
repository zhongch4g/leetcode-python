#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/30 3:26 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 286. Walls and Gates.py
# @Software: IntelliJ IDEA


from collections import deque
class Solution:
    def wallsAndGates(self, rooms) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        # edges case
        if not rooms:
            return
        m, n = len(rooms), len(rooms[0])
        queue = deque([])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        while queue:
            x, y = queue.popleft()
            for cx, cy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx = x + cx
                ny = y + cy
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                if rooms[nx][ny] != 2147483647:
                    continue
                queue.append((nx, ny))
                rooms[nx][ny] = rooms[x][y] + 1
