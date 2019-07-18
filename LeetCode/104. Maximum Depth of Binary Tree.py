#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/18 5:18 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 104. Maximum Depth of Binary Tree.py
# @Software: IntelliJ IDEA


# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        level = {}
        depth = 1
        self.find_depth(root, level, depth)
        return len(level)

    def find_depth(self, root, level, depth):
        if not root:
            return
        level[depth] = root.val
        self.find_depth(root.left, level, depth + 1)
        self.find_depth(root.right, level, depth + 1)

    # more efficient
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque([(root, 1)])
        while queue:
            curr, val = queue.popleft()
            if not curr.left and not curr.right and not queue:
                return val
            if curr.left:
                queue.append((curr.left,val+1))
            if curr.right:
                queue.append((curr.right, val+1))
