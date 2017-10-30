#-*-coding:utf-8 -*-
"""
    # @File    : 617. Merge Two Binary Trees.py
    # @Author  : zhongch4g
    # @Time    : 2017/10/30 10:18
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        newNode = t1
        # 判断其中一个节点为空的情况
        # if t1 is None:
        #     return t2
        # if t2 is None:
        #     return t1
        # 当t1和t2节点都不为空时
        if t1 is not None and t2 is not None:
            t1.val = t1.val + t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
        if t1 is None and t2 is not None:
            return t2
        return t1

    def showTree(self, t):
        if t is None:
            return
        print(t.val)
        if t.left is not None:
            self.showTree(t.left)
        if t.right is not None:
            self.showTree(t.right)


Node = TreeNode(1)
Node.left = TreeNode(3)
Node.left.left = TreeNode(5)
Node.right = TreeNode(2)

Node1 = TreeNode(2)
Node1.left = TreeNode(1)
Node1.left.right = TreeNode(4)
Node1.right = TreeNode(3)
Node1.right.right = TreeNode(7)

Node2 = None

instance = Solution()
root = instance.mergeTrees(Node, Node1)
instance.showTree(root)



