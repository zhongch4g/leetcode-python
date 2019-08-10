#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/10 2:55 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 144. Binary Tree Preorder Traversal.py
# @Software: IntelliJ IDEA


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        res = []
        stack = []
        if root:
            stack.append(root)
        while stack:
            cur = stack.pop()
            res.append(cur.val)
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
        return res

    def preorderTraversal2(self, root):
        res = []
        if not root:
            return res
        self.traversal(root, res)
        return res

    def traversal(self, root, res):
        if not root:
            return

        res.append(root.val)
        self.traversal(root.left, res)
        self.traversal(root.right, res)
