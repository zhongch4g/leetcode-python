#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/10 3:30 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 145. Binary Tree Postorder Traversal.py
# @Software: IntelliJ IDEA


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution: #栈的精髓：把 递归中最后处理 的 压在最前面
    def postorderTraversal(self, root):
        if not root: return []

        res = []
        stack = [(root, False)]
        while stack:
            node, visited = stack.pop()
            if visited:
                res.append(node.val)
            else:
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))

        return res
