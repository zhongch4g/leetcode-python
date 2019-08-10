#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/9 7:53 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 651. Binary Tree Vertical Order Traversal.py
# @Software: IntelliJ IDEA


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def verticalOrder(self, root):
        if not root:
            return []
        queue = deque([(root, 0)])
        res = {}
        minr, maxr = 0, 0
        while queue:
            node, l = queue.popleft()
            if not node:
                continue
            if node.left:
                queue.append((node.left, l - 1))
                minr = min(minr, l - 1)
            if node.right:
                queue.append((node.right, l + 1))
                maxr = max(maxr, l + 1)
            res.setdefault(l, [])
            res[l].append(node.val)
        ret = []
        for i in range(minr, maxr + 1):
            if i not in res:
                break
            ret.append(res[i])
        return ret
