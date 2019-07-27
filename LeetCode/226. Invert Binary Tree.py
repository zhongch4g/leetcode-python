#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/26 7:32 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 226. Invert Binary Tree.py
# @Software: IntelliJ IDEA


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if not root.left and not root.right:
            return root
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.right = left
        root.left = right
        return root

    def invertTree1(self, root):
        if not root:
            return None
        queue = deque([root])
        while queue:
            cur = queue.popleft()
            cur.left, cur.right = cur.right, cur.left
            if cur.left:
                queue.append(cur.left)

            if cur.right:
                queue.append(cur.right)
        return root
