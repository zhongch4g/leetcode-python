#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/19 6:43 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 124. Binary Tree Maximum Path Sum.py
# @Software: IntelliJ IDEA

import sys
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.largest = -sys.maxsize - 1

    def maxPathSum(self, root: TreeNode) -> int:
        maxSum, _ = self.maxPathHelper(root)
        return maxSum

    def maxPathHelper(self, root):
        if root is None:
            return - sys.maxsize - 1, 0

        left = self.maxPathHelper(root.left)
        right = self.maxPathHelper(root.right)
        maxpath = max(left[0], right[0], root.val + left[1] + right[1])
        #if the below path is negative, just make it 0 so that we could 'ignore' it

        single = max(left[1] + root.val, right[1] + root.val, 0)

        return maxpath, single


    def maxPathSum2(self, root):
        if not root:
            return 0
        self.helper(root)
        return self.largest

    def helper(self, root):
        if not root:
            return 0

        leftmax = self.helper(root.left)
        rightmax = self.helper(root.right)

        addroot = root.val + leftmax + rightmax
        single = root.val + max(leftmax, rightmax, 0)
        self.largest = max(self.largest, addroot, single)
        return single