#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/10/3 2:01 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : Remove Extra Edge.py
# @Software: IntelliJ IDEA


class Solution:
    def remove_extra_edge_BT(self, root):
        return self.remove_edge(root, set())

    def remove_edge(self, root, visited):
        if not root or root in visited:
            return None

        visited.add(root)

        root.left = self.remove_edge(root.left, visited)

        root.right = self.remove_edge(root.right, visited)

        return root

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

from collections import deque
def bfs(root):
    res = []
    queue = deque([root])

    while queue:
        size = len(queue)
        lvl = []
        for i in range(size):
            cur = queue.popleft()
            lvl.append(cur)

            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)

        res.append(lvl)


    print(res)


"""
what if it is BST ?
"""
class Solution1:
    def remove_extra_edge_BST(self, root):
        return self.remove_edge(root, None, None)

    def remove_edge(self, root, minimum, maximum):
        if not root:
            return None
        if (minimum and root.val <= minimum) or (maximum and root.val >= maximum):
            return None

        root.left = self.remove_edge(root.left, minimum, root.val)
        root.right = self.remove_edge(root.right, root.val, maximum)

        return root



node1 = Node(3)
node2 = Node(2)
node3 = Node(5)
node4 = Node(1)
node5 = Node(4)
node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node5

solution = Solution()
root = solution.remove_extra_edge_BT(node1)
bfs(root)
print("...")
solution1 = Solution1()
root1 = solution1.remove_extra_edge_BST(node1)
bfs(root1)
