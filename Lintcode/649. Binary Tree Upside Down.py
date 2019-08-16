#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/24 2:42 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 649. Binary Tree Upside Down.py
# @Software: IntelliJ IDEA


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: the root of binary tree
    @return: new root
    """
    def upsideDownBinaryTree(self, root):
        if not root:
            return None
        return self.usd(root)

    def usd(self, root):
        if not root.left:
            return root

        cur_root = self.usd(root.left)

        root.left.right = root
        root.left.left = root.right
        root.left = None
        root.right = None

        return cur_root


