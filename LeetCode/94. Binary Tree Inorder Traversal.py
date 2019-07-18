#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/18 9:19 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 94. Binary Tree Inorder Traversal.py
# @Software: IntelliJ IDEA


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):

        result = []
        self.traverse(root, result)
        print(result)

    def traverse(self, root, result):
        if root is not None:
            self.traverse(root.left, result)
            result.append(root.val)
            self.traverse(root.right, result)


    def inorderTraversal2(self, root):
        result = []
        stack = []
        curr = root
        while curr is not None or not self.is_empty(stack):
            while curr is not None:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        return result


    def is_empty(self, stack):
        return stack == []



node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node1.right = node2
node2.left = node3
solution = Solution()
solution.inorderTraversal2(node1)