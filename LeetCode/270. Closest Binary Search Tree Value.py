#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/3 9:56 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 270. Closest Binary Search Tree Value.py
# @Software: IntelliJ IDEA


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import sys
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:


        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left
        pre = TreeNode(-sys.maxsize - 1)
        while self.stack:
            cur = self.next()
            if pre.val <= target <= cur.val:
                return cur.val if target - pre.val > cur.val - target else pre.val

            pre = cur
        return pre.val


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


