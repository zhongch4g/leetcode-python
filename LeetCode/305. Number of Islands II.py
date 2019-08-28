#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/27 4:42 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 305. Number of Islands II.py
# @Software: IntelliJ IDEA


class UF:
    def __init__(self, m, n):
        self.father = [i for i in range(m*n)]
        self.islands = 0

    def union(self, cid, nid):
        root_cid = self.find(cid)
        root_nid = self.find(nid)
        if root_cid != root_nid:
            self.islands -= 1
            self.father[root_cid] = root_nid

    def find(self, a):
        if self.father[a] == a:
            return a
        self.father[a] = self.find(self.father[a])
        return self.father[a]

    def get_islands(self):
        return self.islands


class Solution:
    def get_id(self, n, x, y):
        return x * n + y

    def numIslands2(self, m: int, n: int, positions):
        result = []
        if not positions:
            return result

        grid = [[0] * n for i in range(m)]

        uf = UF(m, n)

        path = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for position in positions:
            x, y = position[0], position[1]
            cid = self.get_id(n, x, y)
            if grid[x][y] != 1:
                uf.islands += 1
                grid[x][y] = 1
                for _x, _y in path:
                    nx = x + _x
                    ny = y + _y
                    nid = self.get_id(n, nx, ny)
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        uf.union(cid, nid)
            result.append(uf.get_islands())
        return result
