#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/28 2:33 PM
# @Author  : zhongch4g
# @Site    : 
# @File    : 236. Lowest Common Ancestor of a Binary Tree.py
# @Software: IntelliJ IDEA


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        has_p = self.search(root, p)
        has_q = self.search(root, q)

        if has_p and has_q:
            return self.find_lca(root, p, q)
        else:
            return "No Lca"

    def search(self, root, r):

        if not root:
            return False

        if root == r:
            return True

        left = self.search(root.left, r)
        right = self.search(root.right, r)
        return left or right


    def find_lca(self, root, p, q):
        # p & 下面有q return p
        # q & 下面有p return q
        # p & 下面什么都没 return p
        # q & 下面什么都没 return q
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


root = TreeNode(0)
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
root.left = node1
root.right = node2
solution = Solution()
res = solution.lowestCommonAncestor(root, node1, node3)
print(res.val if type(res) == TreeNode else res)