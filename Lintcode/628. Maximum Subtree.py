#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/23 4:23 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 628. Maximum Subtree.py
# @Software: IntelliJ IDEA


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

import sys
class Solution:
    """
    @param root: the root of binary tree
    @return: the maximum weight node
    """
    def __init__(self):
        self.maximum = - sys.maxsize - 1
        self.result = None

    def findSubtree(self, root):
        if not root:
            return None
        self.maximum = self.search(root)
        return self.result

    # left tree max & right tree max & its node
    def search(self, root):
        # base case
        if not root:
            return 0

        leftmax = self.search(root.left)
        rightmax = self.search(root.right)

        # 最大子树指的是整棵子树
        if leftmax + rightmax + root.val > self.maximum or not self.result:
            self.maximum = leftmax + rightmax + root.val
            self.result = root
        return leftmax + rightmax + root.val
