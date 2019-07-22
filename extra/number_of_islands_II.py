#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/5 1:28 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : number_of_islands_II.py
# @Software: IntelliJ IDEA

"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    """
    @param n: An integer
    @param m: An integer
    @param operators: an array of point
    @return: an integer array
    """

    class UnionFind:
        def __init__(self, n, m):
            self.hash = {}
            for i in range(n):
                for j in range(m):
                    id = i * m + j
                    self.hash[id] = self.hash.get(id, id)

        def compress_find(self, x):
            father = self.hash[x]
            while father != self.hash[father]:
                father = self.hash[father]

            t = x
            while t != self.hash.get(t):
                temp = self.hash.get(t)
                self.hash[t] = father
                t = temp
            return father

        def union(self, a, b):
            root_a = self.compress_find(a)
            root_b = self.compress_find(b)
            if root_a != root_b:
                self.hash[root_a] = root_b

    def numIslands2(self, n, m, operators):
        ans = []
        if not operators:
            return ans
        islands = [[0]*m for i in range(n)]
        _x = [0, 0, -1, 1]
        _y = [1, -1, 0, 0]
        uf = self.UnionFind(n, m)
        count = 0
        for operate in operators:
            x = operate.x
            y = operate.y
            if islands[x][y] != 1:
                islands[x][y] = 1
                count += 1
                oid = x * m + y

                for path in range(4):
                    n_x = x + _x[path]
                    n_y = y + _y[path]
                    if 0 <= n_x < n and 0 <= n_y < m and islands[n_x][n_y] == 1:
                        nid = n_x * m + n_y
                        fa = uf.compress_find(oid)
                        nfa = uf.compress_find(nid)

                        if fa != nfa:
                            count -= 1
                            uf.union(fa, nfa)
            ans.append(count)
        return ans


node = [[1,1],[1,2],[1,3],[1,4]]
point = []
for p in node:
    point.append(Point(p[0], p[1]))

solution = Solution()
ans = solution.numIslands2(4, 5, point)
print(ans)

