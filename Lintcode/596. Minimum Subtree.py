#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 1:33 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 596. Minimum Subtree.py
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
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        minimum, tree, sum = self.find(root)
        return tree

    def find(self, root):
        if not root:
            return sys.maxsize, None, 0

        left_minimum, left_root, left_sum = self.find(root.left)
        right_minimum, right_root, right_sum = self.find(root.right)

        sum = left_sum + right_sum + root.val
        if left_minimum == min(sum, left_minimum, right_minimum):
            return left_minimum, left_root, sum

        if right_minimum == min(sum, left_minimum, right_minimum):
            return right_minimum, right_root, sum

        return sum, root, sum