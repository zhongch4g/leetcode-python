#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/18 5:31 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 105. Construct Binary Tree from Preorder and Inorder Traversal.py
# @Software: IntelliJ IDEA


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        return self.build(preorder, 0, inorder, 0, len(inorder) - 1)


    def build(self, preorder, index, inorder, left, right):
        if index > len(preorder) - 1 or left > right:
            return None

        root = TreeNode(preorder[index])
        ind = inorder.index(preorder[index])

        root.left = self.build(preorder, index + 1, inorder, left, ind - 1)
        root.right = self.build(preorder, index + ind - left + 1, inorder, ind + 1, right)

        return root



preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
solution = Solution()
solution.buildTree(preorder, inorder)
