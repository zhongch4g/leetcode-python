#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 8:36 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 230. Kth Smallest Element in a BST.py
# @Software: IntelliJ IDEA


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        while root:
            stack.append(root)
            root = root.left

        for i in range(k - 1):
            if not stack:
                return 0
            if stack[-1].right:
                n = stack[-1].right
                while n:
                    stack.append(n)
                    n = n.left
            else:
                n = stack.pop()
                while stack and stack[-1].right == n:
                    n = stack.pop()
        return stack[-1].val