#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/28 9:49 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 480. Binary Tree Paths.py
# @Software: IntelliJ IDEA


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths1(self, root):
        if not root:
            return []
        results = []
        self.helper1(root, [str(root.val)], results)
        return results

    def helper1(self, root, result, results):

        if not root.left and not root.right:
            results.append('->'.join(result))

            return

        if root.left:
            result.append(str(root.left.val))
            self.helper1(root.left, result, results)
            results.pop()
        if root.right:
            result.append(str(root.right.val))
            self.helper1(root.right, result, results)
            results.pop()


    def binaryTreePaths(self, root):
        if not root:
            return []
        results = []
        self.helper(root, [], results)
        return results

    def helper(self, root, result, results):
        result.append(str(root.val))

        if not root.left and not root.right:
            results.append('->'.join(result))
            result.pop()
            return

        if root.left:
            self.helper(root.left, result, results)
        if root.right:
            self.helper(root.right, result, results)

        result.pop()
