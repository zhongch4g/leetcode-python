#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/28 2:53 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 596. Mininum Subtree.py
# @Software: IntelliJ IDEA

import sys
class Solution:
    def findSubtree(self, root):

        mininum, subtree, sum = self.helper(root)
        return subtree

    def helper(self, root):
        if not root:
            return sys.maxsize, None, 0

        left_minimum, left_subtree, left_sum = self.helper(root.left)
        right_minimum, right_subtree, right_sum = self.helper(root.left)

        sum = left_sum + right_sum + root.val

        if left_minimum == min(left_minimum, right_minimum, sum):
            return left_minimum, left_subtree, sum

        if right_minimum == min(left_minimum, right_minimum, sum):
            return right_minimum, right_subtree, sum

        return sum, root, sum