#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/27 9:51 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 261. Graph Valid Tree.py
# @Software: IntelliJ IDEA


class Solution:
    def validTree(self, n: int, edges) -> bool:
        if n - 1 != len(edges):
            return False

        self.father = [i for i in range(n)]

        for node1, node2 in edges:
            if self.find(node1) == self.find(node2):
                return False
            self.union(node1, node2)
        return True

    def find(self, node):
        if node == self.father[node]:
            return node
        self.father[node] = self.find(self.father[node])
        return self.father[node]

    def union(self, node1, node2):
        root_node1 = self.find(node1)
        root_node2 = self.find(node2)
        if root_node1 != root_node2:
            self.father[root_node1] = root_node2


solution = Solution()
res = solution.validTree(5, [[0,1],[0,4],[1,4],[2,3]])
print(res)