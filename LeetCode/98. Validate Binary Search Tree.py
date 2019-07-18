#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/18 11:48 AM
# @Author  : zhongch4g
# @Site    : 
# @File    : 98. Validate Binary Search Tree.py
# @Software: IntelliJ IDEA

import sys


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        # traverse this tree

        if not root:
            return True

        if self.is_left_lesser(root.left, root.val) and self.is_right_greater(root.right, root.val) \
            and self.isValidBST(root.left) and self.isValidBST(root.right):
            return True
        else:
            return False

    def is_left_lesser(self, root, val):
        if not root:
            return True
        # 严格小于val
        if root.val >= val:
            return False

        return self.is_left_lesser(root.left, val) and self.is_left_lesser(root.right, val)

    def is_right_greater(self, root, val):
        if not root:
            return True
        # 严格大于val
        if root.val <= val:
            return False

        return self.is_right_greater(root.left, val) and self.is_right_greater(root.right, val)


    def isValidBST2(self, root: TreeNode) -> bool:

        return self.is_valid_bst(root, -sys.maxsize - 1, sys.maxsize)

    def is_valid_bst(self, root, minint, maxint):
        if not root:
            return True

        if root.val <= minint or root.val >= maxint:
            return False

        if self.is_valid_bst(root.left, minint, root.val) and \
            self.is_valid_bst(root.right, root.val, maxint):
            return True
        else:
            return False


    # 递归版
    def isValidBST3(self, root: TreeNode) -> bool:

        result = []
        self.inorder_traverse(root, result)

        for i in range(len(result)):
            if i > 0 and result[i] <= result[i-1]:
                return False
        return True

    def inorder_traverse(self, root, result):

        if root is not None:
            self.inorder_traverse(root.left, result)
            result.append(root.val)
            self.inorder_traverse(root.right, result)

    # 迭代版
    def isValidBST4(self, root: TreeNode) -> bool:

        result = []
        self.inorder_traverse_iteration(root, result)

        for i in range(len(result)):
            if i > 0 and result[i] <= result[i-1]:
                return False
        return True

    def inorder_traverse_iteration(self, root, result):
        stack = []
        curr = root
        while curr is not None or not self.is_empty(stack):
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right


        return result

    def is_empty(self, stack):
        return stack == []



