#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/28 10:32 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 1311. Lowest Common Ancestor of a Binary Search Tree.py
# @Software: IntelliJ IDEA


"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: root of the tree
    @param p: the node p
    @param q: the node q
    @return: find the LCA of p and q
    """
    # Binary search tree
    def lowestCommonAncestor1(self, root, p, q):
        # Value of current node or parent node.
        parent_val = root.val

        # Value of p
        p_val = p.val

        # Value of q
        q_val = q.val

        # If both p and q are greater than parent
        if p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right, p, q)
        # If both p and q are lesser than parent
        elif p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left, p, q)
        # We have found the split point, i.e. the LCA node.
        else:
            return root


    def lowestCommonAncestor(self, root, p, q):
        if root is None or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)


        # p, q 一边一个
        if left and right:
            return root

        # 左子树有一个点 或者 左子树有LCA
        if left:
            return left

        # 右子树有一个点 或者 右子树有LCA
        if right:
            return right

        # 左右子树什么都没有
        return None