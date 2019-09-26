#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/25 11:40 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : watering_tree.py
# @Software: IntelliJ IDEA

class tree_node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.to_left_cost = 0
        self.to_right_cost = 0


class Solution:
    def time_cost(self, root):
        self.all_cost = 0
        self.search(root, 0)
        return self.all_cost

    def search(self, root, cur_sum):
        if not root.left and not root.right:
            self.all_cost = max(cur_sum, self.all_cost)
        if root.left:
            self.search(root.left, cur_sum + root.to_left_cost)
        if root.right:
            self.search(root.right, cur_sum + root.to_right_cost)


root = tree_node(0)
root.to_left_cost = 1
root.to_right_cost = 2
root1 = tree_node(1)
root1.to_left_cost = 3
root1.to_right_cost = 4
root2 = tree_node(2)
root3 = tree_node(3)
root4 = tree_node(4)

root.left = root1
root.right = root2
root1.left = root3
root1.right = root4


solution = Solution()
res = solution.time_cost(root)
print("tree longest path: ", res)

##################################################################################
"""
有向无环图
"""
import sys
class AdjListNode:
    def __init__(self, _v, _weight):
        self.v = _v
        self.weight = _weight

class Graph:
    def __init__(self, capacity):
        self.capacity = capacity
        self.adj = [[] for _ in range(capacity)]

    def add_age(self, u, v, w):
        aln = AdjListNode(v, w)
        self.adj[u].append(aln)

    def longest_path(self, start):
        stack  = []
        visited = [False] * self.capacity
        distance = [- sys.maxsize - 1] * self.capacity
        distance[start] = 0
        for i in range(self.capacity):
            if not visited[i]:
                self.topology_sort_util(i, visited, stack)
        maxd = - sys.maxsize - 1
        # get topology order and store in stack
        while stack:
            u = stack.pop()
            if distance[u] != - sys.maxsize - 1:
                for child in self.adj[u]:
                    if distance[child.v] < distance[u] + child.weight:
                        distance[child.v] = distance[u] + child.weight
                        maxd = max(maxd, distance[child.v])
        print("DAG longest path: ", maxd)

    def topology_sort_util(self, i, visited, stack):
        visited[i] = True
        for child in self.adj[i]:
            if not visited[child.v]:
                self.topology_sort_util(child.v, visited, stack)
        stack.append(i)


graph = Graph(6)
graph.add_age(0, 1, 1)
graph.add_age(0, 2, 2)
graph.add_age(1, 3, 3)
graph.add_age(2, 3, 4)
graph.add_age(3, 5, 5)
graph.add_age(3, 4, 6)
graph.longest_path(2)








