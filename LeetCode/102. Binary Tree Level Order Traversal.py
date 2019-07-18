#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/18 5:02 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 102. Binary Tree Level Order Traversal.py
# @Software: IntelliJ IDEA

from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 层次遍历
    def levelOrder(self, root):
        if not root:
            return []

        queue = deque([root])
        results = []
        while queue:
            length = len(queue)
            temp = []
            for i in range(length):
                curr = queue.popleft()
                if not curr:
                    continue
                temp.append(curr.val)
                queue.append(curr.left)
                queue.append(curr.right)
            if temp:
                results.append(temp)
        return results



