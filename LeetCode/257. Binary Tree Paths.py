#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 2:49 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 257. Binary Tree Paths.py
# @Software: IntelliJ IDEA


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode):
        if not root:
            return []

        results = []
        self.search(root, [str(root.val)], results)
        return results

    def search(self, root, result, results):
        if not root.left and not root.right:
            results.append('->'.join(result))
            return

        if root.left:
            result.append(str(root.left.val))
            self.search(root.left, result, results)
            result.pop()

        if root.right:
            result.append(str(root.right.val))
            self.search(root.right, result, results)
            result.pop()
