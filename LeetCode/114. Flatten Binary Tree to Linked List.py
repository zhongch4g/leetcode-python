#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/19 11:33 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 114. Flatten Binary Tree to Linked List.py
# @Software: IntelliJ IDEA


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        self.flatten(root.right)
        self.flatten(root.left)

        root.right = self.prev
        root.left = None
        self.prev = root
