#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/11 4:02 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 106. Construct Binary Tree from Inorder and Postorder Traversal.py
# @Software: IntelliJ IDEA


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):

        in_idx = {v: idx for idx, v in enumerate(inorder)}
        return self.helper(postorder, inorder, 0, len(inorder) - 1, in_idx)

    def helper(self, postorder, inorder, left, right, in_idx):
        if left > right:
            return None

        val = postorder.pop()
        root = TreeNode(val)
        idx = in_idx[val]
        root.right = self.helper(postorder, inorder, idx + 1, right, in_idx)
        root.left = self.helper(postorder, inorder, left, idx - 1, in_idx)


        return root