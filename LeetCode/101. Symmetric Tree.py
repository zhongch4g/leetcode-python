#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/18 4:26 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 101. Symmetric Tree.py
# @Software: IntelliJ IDEA


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # boundary case
        if not root:
            return True

        return self.compare(root.left, root.right)

    def compare(self, left, right):
        if not left and not right:
            return True

        if left and right and left.val == right.val and \
                self.compare(left.left, right.right) and \
                self.compare(left.right, right.left):
            return True
        else:
            return False

    # Iterative
    def isSymmetric2(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = [root.left, root.right]
        while stack:
            node1, node2 = stack.pop(), stack.pop()
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            stack.append(node1.right)
            stack.append(node2.left)
            stack.append(node1.left)
            stack.append(node2.right)
        return True



node1 = TreeNode(1)
node2, node3 = TreeNode(2), TreeNode(2)
node4, node5 = None, TreeNode(3)
node6, node7 = None, TreeNode(3)
node1.left, node1.right = node2, node3
node2.left, node2.right = node4, node5
node3.left, node3.right = node6, node7

solution = Solution()
res = solution.isSymmetric2(node1)
print(res)

