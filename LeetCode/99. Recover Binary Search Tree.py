#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 8:25 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 99. Recover Binary Search Tree.py
# @Software: IntelliJ IDEA


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left
        x, y = -1, -1
        pre = None
        # find value that next val will smaller than curr node val
        while self.has_next():
            if not pre:
                pre = self.next()
                continue
            cur = self.next()
            if pre.val > cur.val:
                y = cur
                if x == -1:
                    x = pre
                else:
                    break
            pre = cur
        print(x, y)
        x.val, y.val = y.val, x.val

    def next(self):
        node = self.stack[-1]
        if node.right:
            n = node.right
            while n:
                self.stack.append(n)
                n = n.left
        else:
            n = self.stack.pop()
            while self.stack and self.stack[-1].right == n:
                n = self.stack.pop()
        return node


    def has_next(self):
        return len(self.stack) > 0