#-*-coding:utf-8 -*-
"""
    # @File    : 563. Binary Tree Tilt.py
    # @Author  : zhongch4g
    # @Time    : 2017/11/1 15:41
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """


        self.findTilt(root.left)
