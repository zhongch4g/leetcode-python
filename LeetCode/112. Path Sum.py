#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/10 5:48 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 112. Path Sum.py
# @Software: IntelliJ IDEA


class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        sum -= root.val
        if not root.left and not root.right:  # if reach a leaf
            return sum == 0
        left = self.hasPathSum(root.left, sum)
        right = self.hasPathSum(root.right, sum)
        return left or right