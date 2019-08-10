#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/9 10:56 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 103. Binary Tree Zigzag Level Order Traversal.py
# @Software: IntelliJ IDEA


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from collections import deque
class Solution:
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        ret = []
        order = 0
        queue = deque([root])
        while queue:
            level = []
            size = len(queue)
            for i in range(size):
                curr_node = queue.popleft()
                level.append(curr_node.val)
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

            if order & 1:
                level = level[::-1]
            order += 1
            ret.append(level)
        return ret
