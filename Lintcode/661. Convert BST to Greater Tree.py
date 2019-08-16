#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/15 2:34 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 661. Convert BST to Greater Tree.py
# @Software: IntelliJ IDEA


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the new root
    def convertBST(self, root):
        # Write your code here
        self.sum = 0
        self.helper(root)
        return root

    def helper(self, root):
        if root is None:
            return
        if root.right:
            self.helper(root.right)

        self.sum += root.val
        root.val = self.sum
        if root.left:
            self.helper(root.left)