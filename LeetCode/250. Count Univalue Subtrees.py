#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/10 5:56 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 250. Count Univalue Subtrees.py
# @Software: IntelliJ IDEA

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import sys
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        is_unival, rval, cnt = self.cnt_unival_subtree(root)
        return cnt

    def cnt_unival_subtree(self, root):
        if not root:
            return True, sys.maxsize, 0

        if not root.left and not root.right:
            return True, root.val, 1

        left_is_unival, lrval, cnt1 = self.cnt_unival_subtree(root.left)
        right_is_unival, rrval, cnt2 = self.cnt_unival_subtree(root.right)

        if left_is_unival and right_is_unival and \
                ((lrval == root.val and rrval == root.val) or (lrval == root.val and rrval == sys.maxsize) \
                         or (lrval == sys.maxsize and rrval == root.val)):
            return True, root.val, cnt1 + cnt2 + 1
        return False, root.val, cnt1 + cnt2