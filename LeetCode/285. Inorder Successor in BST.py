#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 7:55 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 285. Inorder Successor in BST.py
# @Software: IntelliJ IDEA



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

        while self.has_next():
            cur = self.next()
            if cur == p:
                return self.next() if self.has_next() else None

    def next(self):
        node = self.stack[-1]
        # if node.right is not None
        if node.right:
            n = node.right
            while n:
                self.stack.append(n)
                n = n.left
        # is node.right is None
        else:
            n = self.stack.pop()
            while self.stack and self.stack[-1].right == n:
                n = self.stack.pop()

        return node.val

    def has_next(self):
        return len(self.stack) > 0


