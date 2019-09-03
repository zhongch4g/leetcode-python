#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/2 5:22 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 173. Binary Search Tree Iterator.py
# @Software: IntelliJ IDEA


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
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

            # delete if it is right children
            while self.stack and self.stack[-1].right == n:
                n = self.stack.pop()

        return node.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0


        # Your BSTIterator object will be instantiated and called as such:
        # obj = BSTIterator(root)
        # param_1 = obj.next()
        # param_2 = obj.hasNext()