#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/15 6:07 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 448. Inorder Successor in BST.py
# @Software: IntelliJ IDEA


"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # write your code here

        if not root or not p:
            return None

        if p.val >= root.val:
            return self.inorderSuccessor(root.right, p)

        else:
            left = self.inorderSuccessor(root.left, p)
            return left if left else root

