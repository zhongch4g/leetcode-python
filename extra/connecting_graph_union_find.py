#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/5 8:53 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : connecting_graph_union_find.py
# @Software: IntelliJ IDEA



"""
task introduction: n node graph, no edge
two operator
1.connect a and b : connecting()
2.query a and b connected or not : query()
3.find x's boss : find()
4.find the size of node x : query_size()
"""
class UnionFind:
    def __init__(self, n):
        self.father = [0]
        self.size = [0]
        self.count = n
        for i in range(1, n + 1):
            self.father.append(i)
            self.size.append(1)

    # find node's boss
    def find(self, x):
        if self.father[x] == x:
            return x
        self.father[x] = self.find(self.father[x])
        return self.father[x]

    def connecting(self, a, b):
        find_a = self.find(a)
        find_b = self.find(b)
        if find_a != find_b:
            self.father[find_a] = find_b
            self.size[find_b] += self.size[find_a]
            self.count -= 1

    # to check a, b 's boss is equal or not
    def query(self, a, b):
        find_a = self.find(a)
        find_b = self.find(b)
        return find_a == find_b

    # the size of x's boss(x所在联通块节点个数)
    def query_size(self, x):
        find_x = self.find(x)
        return self.size[find_x]

    def query_area(self):
        return self.count


union_find = UnionFind(10)
